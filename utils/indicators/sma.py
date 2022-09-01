def sma(candles, OHLC):
    prices = []

    try:
        for i in OHLC[::-1][:candles]:
            prices.append(float(i[4]))
        return (sum(prices)/candles)
    except:
        raise ValueError(OHLC['error'])
