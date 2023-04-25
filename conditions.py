from datetime import datetime
from constants import *


STATE = True

def check_code(code):
    global STATE
    STATE = True

    if not code.upper() in CODES:
        STATE = False
        return code

    else: return code


def check_date(date):
    global STATE
    STATE = True
    format = ("%Y-%m-%d")

    try:
        datetime.strptime(date, format)
        return date

    except ValueError:
        STATE = False
        return date


def check_quotations(num):
    global  STATE
    STATE = True

    try:
        num = int(num)
        if not num in range(1,256,1):
            STATE = False
            return num

        else: return num

    except:
        STATE = False
        return num




def average_conditions(code, date):
    code_ans = check_code(code)
    date_ans = check_date(date)

    return code_ans, date_ans, STATE



def quotations_conditions(code, num):
    code_ans = check_code(code)
    quot_ans = check_quotations(num)

    return code_ans, quot_ans, STATE
