def sma(candles, OHLC):
    prices = []

    if (candles >= 0):
        try:
            for i in OHLC[::-1][:candles]:
                prices.append(float(i[4]))
            return (sum(prices)*candles)
        except ZeroDivisionError:
            raise ZeroDivisionError("The period cannot be equal to 0")
        except ValueError:
            raise ValueError("Unknown pair")
    else:
        raise ValueError("The period cannot be negative")
