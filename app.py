from flask import Flask, render_template, request
import url_requests
from data_managment import ExchangeRate


AVERAGE, MIN, MAX, DIFF = None, None, None, None


app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def main():
    global AVERAGE, MIN, MAX, DIFF

    if request.method == "POST":

        code, date, quotations = request.form.get("code"), request.form.get("date"), request.form.get("quotations")
        rate = ExchangeRate(data = None)

        if request.form.get("submit_button") == "Average":
            rate.data = url_requests.average_rate_url(code, date)
            AVERAGE = rate.get_average_rate()


        elif request.form.get("submit_button") == "Min and max":
            rate.data = url_requests.average_rates_url(code, int(quotations))
            MIN, MAX = rate.get_min_max_value()


        elif request.form.get("submit_button") == "Difference":
            rate.data =url_requests.ask_bid_url(code, int(quotations))
            DIFF = rate.get_major_diff()



    return render_template('website.html', rate_1 = AVERAGE, rate_2 = (MIN, MAX), rate_3 = DIFF )

