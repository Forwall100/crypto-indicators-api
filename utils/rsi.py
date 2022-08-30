from statistics import mean
import requests
from .config import intervals


def rsi(interval, candles, symbol):
    url = f"https://api.kraken.com/0/public/OHLC?pair={symbol}&interval={intervals[interval]}"
    response = requests.get(url).json()

    green = []
    red = []

    try:
        for i in response["result"][list(response["result"].keys())[0]][::-1][:candles]:
            open = float(i[1])
            close = float(i[4])
            if open > close:
                red.append(open-close)
            else:
                green.append(close-open)
        result = 100 - 100/(1 + mean(green)/mean(red))
        return result
    except:
        raise ValueError(response['error'])
