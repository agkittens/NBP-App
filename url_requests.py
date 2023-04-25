import urllib.request, json
from constants import *

def check_existance(url:str) -> list or None:

    try:
        urllib.request.urlopen(url)
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        return data

    except: return False


def average_rate_url(code:str, date:str) -> str:
    url = BASE_URL + f"a/{code}/{date}"
    return check_existance(url)

def average_rates_url(code:str, quatations_num:int) -> str:
    url = BASE_URL + f"a/{code}/last/{quatations_num}"
    return check_existance(url)

def ask_bid_url(code:str, quatations_num:int) -> str:
    url = BASE_URL + f"c/{code}/last/{quatations_num}"
    return check_existance(url)

