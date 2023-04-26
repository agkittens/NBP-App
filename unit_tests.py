from data_managment import ExchangeRate
from app import app

#Testing class - each function tests possible choices
#There are 3 functions for correct values - testing if the output is correct (based on value from url)

#There are 3 functions for wrong values - each function has 3 combinations for incorrect output
# (2 with 1 wrong value and 1 with 2 wrong values)


class TestApp:
    rate = ExchangeRate(data = None)
    last_mid_url = "http://api.nbp.pl/api/exchangerates/rates/a/gbp/last/10/"
    last_diff_url = "http://api.nbp.pl/api/exchangerates/rates/c/gbp/last/10/"


    #test if server is online
    def test_server(self):
        with app.test_client() as a:
            response = a.get('/')
            assert response.status_code == 200


    def test_correct_average_data(self):
        code = "gbp"
        date = "2023-04-24"
        correct_value = 5.2176

        average = self.rate.get_average_rate(code, date)
        assert average == correct_value


    def test_correct_min_max_data(self):
        code = "gbp"
        quotations = 10
        correct_number = 2

        self.rate.last_quotations_init(code, quotations, action = "min_max")
        min, max = self.rate.get_min_max_value()

        response = [min, max]
        response = len(response)

        assert response == correct_number


    def test_correct_diff_data(self):
        code = "gbp"
        quotations = 10
        correct_num_of_characters = 76

        self.rate.last_quotations_init(code, quotations, action="diff")
        diff = self.rate.get_major_diff()
        diff = len(diff)

        assert diff == correct_num_of_characters


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

    test.test_server()

    test.test_correct_diff_data()
    test.test_correct_average_data()
    test.test_correct_min_max_data()

    test.test_wrong_average_data()
    test.test_wrong_quotations_data()
