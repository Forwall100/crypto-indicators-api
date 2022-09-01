from ..get_OHLC import kraken_OHLC
from .sma import sma


def ema(interval, candles, pair):
    OHLC = kraken_OHLC(pair, interval)
    result = [sma(interval, candles, pair)]
    k = 2/(candles+1)

    try:
        for price in OHLC:
            price = float(price[4])
            result.append((price-result[-1])*k+result[-1])

        return (result[-1])
    except:
        raise ValueError(OHLC['error'])
