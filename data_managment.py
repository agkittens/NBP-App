import conditions, url_requests

class ExchangeRate:

    def __init__(self, data):
        self.incorrect_info = "Incorrect data"

        try:
            self.data = data
        except:
            self.data = None



    def get_average_rate(self, code, date):
        code, date, state = conditions.average_conditions(code, date)

        if state == True:
            self.data = url_requests.average_rate_url(code, date)

            if self.data is not False:
                average_rate = self.calc_average_rate()
                return average_rate

            else: return self.incorrect_info
        else: return self.incorrect_info



    def last_quotations_init(self, code, quotations, action):
        code, quotations, state = conditions.quotations_conditions(code, quotations)

        if state == True and action == "min_max":
            self.data = url_requests.average_rates_url(code, int(quotations))
            return self.data is not False

        elif state == True and action == "diff":
            self.data = url_requests.ask_bid_url(code, int(quotations))
            return self.data is not False

        else: return False



    def calc_average_rate(self) -> int:
        val = self.data["rates"][0]["mid"]
        return val


    def get_major_diff(self) -> str:
        diff = []
        for x in self.data["rates"]:
            diff.append(format(x["ask"] - x["bid"], ".4"))

        diff = str(diff)[1:-1]
        diff = diff.replace("\'", "")

        return diff



    def get_min_max_value(self) -> tuple:
        values = []

        for x in self.data["rates"]:
            values.append(x["mid"])

        min, max = self.bubble_sort(values)
        return min, max



    def bubble_sort(self,val:list) -> tuple:
        for x in range(len(val)):

            for y in range(len(val) - x - 1):
                if val[y] > val[y + 1]:
                    val[y], val[y + 1] = val[y + 1], val[y]

        min, max = val[0], val[-1]
        return min, max
