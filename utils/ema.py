import requests
from .config import intervals

intervals = {
    "1m": 1,
    "5m": 5,
    "15m": 15,
    "30m": 30,
    "1h": 60,
    "4h": 240,
    "1d": 1440,
    "1w": 10080
}


def ema(interval, candles, symbol):
    url = f"https://api.kraken.com/0/public/OHLC?pair={symbol}&interval={intervals[interval]}"
    response = requests.get(url).json()

    prices = []
    result = [sum(prices[:candles])/candles]
    k = 2/(candles+1)
    try:
        for i in response["result"][list(response["result"].keys())[0]]:
            prices.append(float(i[4]))

        for price in prices:
            result.append((price-result[-1])*k+result[-1])

        return (result[-1])
    except:
        raise ValueError(response['error'])
