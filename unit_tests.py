from data_managment import ExchangeRate

#Testing class - each function tests possible choices
#There are 3 functions for correct values - testing if the output is correct (based on value from url)

#There are 3 functions for wrong values - each function has 3 combinations for incorrect output
# (2 with 1 wrong value and 1 with 2 wrong values)


class TestApp:
    rate = ExchangeRate(data = None)

    def test_correct_average_data(self):
        code = "gbp"
        date = "2023-04-24"
        correct_value = 5.2176

        average = self.rate.get_average_rate(code, date)
        assert average == correct_value


    def test_correct_min_max_data(self):
        code = "gbp"
        quotations = 10
        correct_values = (5.1958, 5.3041)

        self.rate.last_quotations_init(code, quotations, action = "min_max")
        min, max = self.rate.get_min_max_value()

        assert min, max == correct_values


    def test_correct_diff_data(self):
        code = "gbp"
        quotations = 10
        correct_values = "0.1062, 0.1058, 0.105, 0.1048, 0.1048, 0.1048, 0.1048, 0.1044, 0.1042, 0.104"

        self.rate.last_quotations_init(code, quotations, action="diff")
        diff = self.rate.get_major_diff()

        assert diff == correct_values


    def test_wrong_average_data(self):
        correct_code = "gbp"
        wrong_code = "xdd"

        correct_date = "2023-04-24"
        wrong_date = "2023-04-22"  #weekend

        wrong_value = "Incorrect data"

        average_wrong_1 = self.rate.get_average_rate(wrong_code, correct_date)
        average_wrong_2 = self.rate.get_average_rate(correct_code, wrong_date)
        average_wrong_3 = self.rate.get_average_rate(wrong_value, wrong_date)

        assert average_wrong_1 == wrong_value
        assert average_wrong_2 == wrong_value
        assert average_wrong_3 == wrong_value


    def test_wrong_quotations_data(self):
        correct_code = "gbp"
        wrong_code = "xdd"

        correct_quotat = 10
        wrong_quotat = -1  #not in range (1, 256)

        wrong_value = False

        input_wrong1 = self.rate.last_quotations_init(correct_code, wrong_quotat, action = "min_max")
        input_wrong2 = self.rate.last_quotations_init(wrong_code, correct_quotat, action = "min_max")
        input_wrong3 = self.rate.last_quotations_init(wrong_code, wrong_quotat, action = "min_max")

        assert input_wrong1 == wrong_value
        assert input_wrong2 == wrong_value
        assert input_wrong3 == wrong_value


if __name__=='__main__':
    test = TestApp()

    test.test_correct_diff_data()
    test.test_correct_average_data()
    test.test_correct_min_max_data()

    test.test_wrong_average_data()
    test.test_wrong_quotations_data()
