import requests
from .constans import intervals


def kraken_OHLC(pair, interval):
    try:
        url = f"https://api.kraken.com/0/public/OHLC?pair={pair}&interval={intervals[interval]}"
        response = requests.get(url).json()
        return response["result"][list(response["result"].keys())[0]]
    except ValueError:
        raise ValueError("Unknown pair")
