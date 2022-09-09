from statistics import mean
from unittest import result


def rsi(candles, OHLC):
    green = []
    red = []

    if candles > 0:
        try:
            for i in OHLC[::-1][:candles]:
                open = float(i[1])
                close = float(i[4])
                if open > close:
                    red.append(open-close)
                else:
                    green.append(close-open)
            if len(green) == 0:
                result = 0
            elif len(red) == 0:
                result = 100
            else:
                result = 100 - 100/(1 + mean(green)/mean(red))
            return round(result, 2)
        except ValueError:
            raise ValueError("Unknown pair")
    elif candles == 0:
        raise ValueError("The period cannot be equal to 0")
    elif candles < 0:
        raise ValueError("The period cannot be negative")
