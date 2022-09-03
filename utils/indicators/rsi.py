from statistics import mean


def rsi(candles, OHLC):
    green = []
    red = []

    if candles > 1:
        try:
            for i in OHLC[::-1][:candles]:
                open = float(i[1])
                close = float(i[4])
                if open > close:
                    red.append(open-close)
                else:
                    green.append(close-open)
            result = 100 - 100/(1 + mean(green)/mean(red))
            return round(result, 2)
        except ValueError:
            raise ValueError("Unkown pair")
    elif candles == 1:
        raise ValueError("The period cannot be equal to 1")
    elif candles == 0:
        raise ValueError("The period cannot be equal to 0")
    elif candles < 0:
        raise ValueError("The period cannot be negative")