import requests
from .config import intervals


def sma(interval, candles, symbol):
    url = f"https://api.kraken.com/0/public/OHLC?pair={symbol}&interval={intervals[interval]}"
    response = requests.get(url).json()

    prices = []
    try:
        for i in response["result"][list(response["result"].keys())[0]][::-1][:candles]:
            prices.append(float(i[4]))
        return (sum(prices)/candles)
    except:
        raise ValueError(response['error'])
