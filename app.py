from flask import Flask, render_template, request
from data_managment import ExchangeRate


MESSAGE = ""
AVERAGE, MIN_MAX, DIFF = MESSAGE, MESSAGE, MESSAGE


app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def main():
    global AVERAGE, MIN_MAX, DIFF

    if request.method == "POST":

        code, date, quotations = request.form.get("code"), request.form.get("date"), request.form.get("quotations")
        rate = ExchangeRate(data = None)



        if request.form.get("submit_button") == "Average":
            AVERAGE = rate.average_rate_init(code, date)



        elif request.form.get("submit_button") == "Min and max":
            if rate.last_quotations_init(code, quotations):
                MIN_MAX = rate.get_min_max_value()

            else: MIN_MAX = rate.incorrect_info



        elif request.form.get("submit_button") == "Difference":
            if rate.last_quotations_init(code, quotations):
                DIFF = rate.get_major_diff()

            else:
                DIFF = rate.incorrect_info



    return render_template('website.html', rate_1 = AVERAGE, rate_2 = MIN_MAX, rate_3 = DIFF )


