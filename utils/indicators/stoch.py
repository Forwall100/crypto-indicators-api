def stoch(k_period, d_period, OHLC):
    K = []

    if k_period > 0 and d_period > 0:
        try:
            for i in range(0, k_period):
                last_closing_price = float(OHLC[::-1][i][4])
                low = []
                hight = []
                for j in OHLC[::-1][:k_period]:
                    low.append(float(j[3]))
                    hight.append(float(j[2]))
                K.append(
                    round(((last_closing_price - min(low))/(max(hight) - min(low)))*100, 2))

            D = round(sum(K[:d_period])/d_period, 2)

            return [K[0], D]
        except ValueError:
            raise ValueError("Unknown pair")
        except ZeroDivisionError:
            raise ZeroDivisionError("Min(low) == Max(high), zero division")
    elif k_period == 0 or d_period == 0:
        raise ValueError("The period cannot be equal to 0")
    elif k_period < 0 or d_period < 0:
        raise ValueError("The period cannot be negative")
