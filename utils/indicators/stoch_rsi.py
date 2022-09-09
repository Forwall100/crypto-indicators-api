import re
from .rsi import rsi


def stoch_rsi(candles, OHLC):
    if candles > 2:
        try:
            rsi_history = []
            OHLC = OHLC[::-1][:candles]
            for i in range(2, len(OHLC)):
                rsi_history.append(rsi(candles, OHLC[:i]))
            if max(rsi_history) == min(rsi_history):
                return max(rsi_history)
            else:
                return round((rsi_history[0]-min(rsi_history))/(max(rsi_history) - min(rsi_history))*100, 2) 
        except ValueError:
            raise ValueError("Unknown pair")
    elif candles == 0:
        raise ValueError("The period cannot be equal to 0")
    elif candles <= 2 and candles > 0:
        raise ValueError("The period must be more than 2")
    elif candles < 0:
        raise ValueError("The period cannot be negative")