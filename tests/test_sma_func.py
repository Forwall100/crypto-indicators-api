from utils.indicators.sma import sma
from .OHLC_test_data import OHLC
import pytest


@pytest.mark.parametrize("candles, expected_result", [
    (1, 20114.9),
    (5, 20094.7),
    (10, 20132.84)
])
def test_good_values(candles, expected_result):
    assert sma(candles, OHLC) == expected_result


def test_zero_candles():
    with pytest.raises(ZeroDivisionError):
        sma(0, OHLC)


def test_negative_candles():
    with pytest.raises(ValueError):
        sma(-1, OHLC)


@pytest.mark.parametrize("candles", [
    ("10"),
    ([10, 11]),
    ({"SMA": 12}),
])
def test_type_candles(candles):
    with pytest.raises(TypeError):
        sma(candles, OHLC)
