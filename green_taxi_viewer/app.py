import io
import matplotlib.pyplot as plt
import datetime as dt

from flask import Flask, render_template, request


app = Flask(__name__)


def predict_trip_costs(h):
    """This is a dummy prediction function, which always predicts
    the average of the next 24 hours copied by hand from synapse.
    In reality, you could have a machine learning model file as part of
    the repository and use that to either train or make predictions.

    Parameters
    ----------
    h : int
        Hour of the day

    Returns
    -------
    list
        Expected normalized trip cost for the coming 24 hours.
    """
    pred = [
        0.0208365, 0.02058832, 0.01781128, 0.01946697, 0.01930636,
        0.01736085, 0.01729656, 0.01700394, 0.01756695, 0.01713748,
        0.01806401, 0.01859311, 0.02019171, 0.01891349, 0.02013918,
        0.02105339, 0.02070073, 0.02223452, 0.02666162, 0.0240056,
        0.02165742, 0.01765045, 0.01760978, 0.01764494,
    ] * 2

    return pred[h:h + 24]


def create_figure(y):
    """Make a lineplot of y and save it as static figure

    Parameters
    ----------
    y : list
    """
    x = range(0, len(y))
    fig = plt.figure()
    plt.plot(x, y)
    plt.xlabel("Hours from now")
    plt.ylabel("Expected costs")
    plt.title("Expected price for the coming 24 hours")
    fig.savefig('./static/images/price_plot.png')


def get_knmi_data():
    """Verbind met de KNMI Api en haal de data op. Probeer environment variables te
    gebruiken die je aan docker mee geeft.
    """
    pass


def plot_knmi_data():
    """BONUS: Define a plotting function based on the examples above
    that shows some weather information from the KNMI data. Save the
    figure in ./static/images and make it appear in the app by changing the
    url variable.
    """
    pass


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def main():
    """Pas deze functie aan zodat KNMI data wordt getoond op de website.
    """

    knmi_data = ""
    instruction_button = "Voorspel de komende 24 uur."
    website_title = "NYC Green Taxi data viewer"

    if request.method == 'POST':

        hour = request.form.get('hour')
        if hour == "now":
            hour = dt.datetime.now().hour

        create_figure(predict_trip_costs(hour))
        return render_template(
            'home.html',
            url='/static/images/price_plot.png',
            instruction_button=instruction_button,
            website_title=website_title,
            knmi_data=knmi_data,
        )

    else:
        return render_template(
            'home.html',
            url=None,
            instruction_button=instruction_button,
            website_title=website_title,
            knmi_data=knmi_data,
        )


if __name__ == "__main__":
    app.run(debug=True)
