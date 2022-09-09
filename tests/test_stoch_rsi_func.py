from utils.indicators.stoch_rsi import stoch_rsi
from .OHLC_test_data import OHLC
import pytest


@pytest.mark.parametrize("candles, expected_result", [
    (100, 0.0),
    (300, 0.0),
])
def test_good_values(candles, expected_result):
    assert stoch_rsi(candles, OHLC) == expected_result


def test_zero_candles():
    with pytest.raises(ValueError):
        stoch_rsi(0, OHLC)


def test_negative_candles():
    with pytest.raises(ValueError):
        stoch_rsi(-1, OHLC)


@pytest.mark.parametrize("candles", [
    ("10"),
    ([10, 11]),
    ({"stoch_rsi", 12})
])
def test_type_candles(candles):
    with pytest.raises(TypeError):
        stoch_rsi(candles, OHLC)
