from statistics import mean


def ema(candles, OHLC):
    result = [mean([float(price[4]) for price in OHLC])]
    k = 2/(candles+1)

    try:
        for price in OHLC:
            price = float(price[4])
            result.append((price-result[-1])*k+result[-1])

        return (result[-1])
    except:
        raise ValueError(OHLC['error'])
