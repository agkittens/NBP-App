from flask import Flask, render_template, request
from data_managment import ExchangeRate


MESSAGE = ""
RATE = ExchangeRate(data = None)

app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def main():
    AVERAGE, MIN_MAX, DIFF, CODE, DATE, QUOTATIONS = MESSAGE, MESSAGE, MESSAGE, MESSAGE, MESSAGE, MESSAGE

    if request.method == "POST":
        CODE, DATE, QUOTATIONS = request.form.get("code"), request.form.get("date"), request.form.get("quotations")


        if request.form.get("submit_button") == "Average":
            AVERAGE = RATE.get_average_rate(CODE, DATE)



        elif request.form.get("submit_button") == "Min and max":
            if RATE.last_quotations_init(CODE, QUOTATIONS, action = "min_max"):
                MIN_MAX = RATE.get_min_max_value()

            else: MIN_MAX = RATE.incorrect_info



        elif request.form.get("submit_button") == "Difference":
            if RATE.last_quotations_init(CODE, QUOTATIONS, action = "diff"):
                DIFF = RATE.get_major_diff()

            else:
                DIFF = RATE.incorrect_info



    return render_template('website.html', rate_1 = AVERAGE, rate_2 = MIN_MAX, rate_3 = DIFF,
                           code = CODE, date = DATE, quotations = QUOTATIONS)


