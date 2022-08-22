import requests

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
