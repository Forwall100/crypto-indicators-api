import requests
from .config import intervals


def sma(interval, candles, symbol):
    url = f"https://api.kraken.com/0/public/OHLC?pair={symbol}&interval={intervals[interval]}"
    response = requests.get(url).json()

    sum_close = 0
    counter = 0
    try:
        for i in response["result"][list(response["result"].keys())[0]][::-1]:
            counter += 1
            if counter <= candles:
                sum_close += float(i[4])
        return (sum_close/candles)
    except:
        raise ValueError(response['error'])
