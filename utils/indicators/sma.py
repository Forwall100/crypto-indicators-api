from ..get_OHLC import kraken_OHLC


def sma(interval, candles, pair):
    OHLC = kraken_OHLC(pair, interval)
    prices = []

    try:
        for i in OHLC[::-1][:candles]:
            prices.append(float(i[4]))
        return (sum(prices)/candles)
    except:
        raise ValueError(OHLC['error'])
