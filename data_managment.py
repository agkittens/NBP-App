import pandas as pd



class ExchangeRate:

    def __init__(self, data):
        try:
            self.data = pd.json_normalize(data)
        except:
            self.data = "Parameter was not provided"


    def get_major_diff(self) -> list:
        diff = []
        for x in self.data["rates"]:
            diff.append(format(x["ask"] - x["bid"], ".4"))

        return diff



    def get_average_rate(self) -> int:
        val = self.data["rates"][0]["mid"]
        return val



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
