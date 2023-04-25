import conditions, url_requests

class ExchangeRate:

    def __init__(self, data):
        self.incorrect_info = "Incorrect data"

        try:
            self.data = data

        except:
            self.data = None



    def average_rate_init(self, code, date):
        code, date, state = conditions.average_conditions(code, date)

        if state == True:
            self.data = url_requests.average_rate_url(code, date)

            if self.data is not False:
                average_rate = self.get_average_rate()
                return average_rate

            else: return self.incorrect_info
        else: return self.incorrect_info



    def last_quotations_init(self, code, quotations):
        code, quotations, state = conditions.quotations_conditions(code, quotations)

        if state == True:
            self.data = url_requests.average_rates_url(code, int(quotations))

            if self.data is not False: return True
            else: return False

        else: return False



    def get_average_rate(self) -> int:
        val = self.data["rates"][0]["mid"]
        return val


    def get_major_diff(self) -> list:
        diff = []
        for x in self.data["rates"]:
            diff.append(format(x["ask"] - x["bid"], ".4"))

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
