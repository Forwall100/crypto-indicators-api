from statistics import mean
from ..get_OHLC import kraken_OHLC


def rsi(interval, candles, pair):
    OHLC = kraken_OHLC(pair, interval)

    green = []
    red = []

    try:
        for i in OHLC[::-1][:candles]:
            open = float(i[1])
            close = float(i[4])
            if open > close:
                red.append(open-close)
            else:
                green.append(close-open)
        result = 100 - 100/(1 + mean(green)/mean(red))
        return result
    except:
        raise ValueError(OHLC['error'])
