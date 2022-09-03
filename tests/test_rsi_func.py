from cgitb import reset
from utils.indicators.rsi import rsi
from .OHLC_test_data import OHLC
import pytest


@pytest.mark.parametrize("candles, expected_result", [
    (5, 49.95),
    (10, 59.91)
])
def test_good_values(candles, expected_result):
    assert rsi(candles, OHLC) == expected_result


def test_zero_candles():
    with pytest.raises(ValueError):
        rsi(0, OHLC)


def test_one_candles():
    with pytest.raises(ValueError):
        rsi(1, OHLC)


def test_negative_candles():
    with pytest.raises(ValueError):
        rsi(-1, OHLC)


@pytest.mark.parametrize("candles", [
    ("10"),
    ([10, 11]),
    ({"RSI", 12})
])
def test_type_candles(candles):
    with pytest.raises(TypeError):
        rsi(candles, OHLC)
