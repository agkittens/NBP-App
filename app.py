from flask import Flask, render_template, request
from data_managment import ExchangeRate


MESSAGE = ""
AVERAGE, MIN_MAX, DIFF = MESSAGE, MESSAGE, MESSAGE
RATE = ExchangeRate(data = None)

app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def main():
    global AVERAGE, MIN_MAX, DIFF

    if request.method == "POST":
        code, date, quotations = request.form.get("code"), request.form.get("date"), request.form.get("quotations")


        if request.form.get("submit_button") == "Average":
            AVERAGE = RATE.average_rate_init(code, date)



        elif request.form.get("submit_button") == "Min and max":
            if RATE.last_quotations_init(code, quotations, action = "min_max"):
                MIN_MAX = RATE.get_min_max_value()

            else: MIN_MAX = RATE.incorrect_info



        elif request.form.get("submit_button") == "Difference":
            if RATE.last_quotations_init(code, quotations, action = "diff"):
                DIFF = RATE.get_major_diff()

            else:
                DIFF = RATE.incorrect_info



    return render_template('website.html', rate_1 = AVERAGE, rate_2 = MIN_MAX, rate_3 = DIFF )


