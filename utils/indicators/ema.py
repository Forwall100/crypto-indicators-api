from statistics import mean


def ema(candles, OHLC):
    if candles > 0:
        try:
            result = [mean([float(price[4]) for price in OHLC])]
            k = 2/(candles+1)
            for price in OHLC:
                price = float(price[4])
                result.append((price-result[-1])*k+result[-1])
            return (round(result[-1], 2))
        except ValueError:
            raise ValueError("Unknown pair")
    elif candles == 0:
        raise ValueError("The period cannot be equal to 0")
    elif candles < 0:
        raise ValueError("The period cannot be negative")
