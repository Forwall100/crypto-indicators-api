from utils.indicators.ema import ema
from .OHLC_test_data import OHLC
import pytest


@pytest.mark.parametrize("candles, expected_result", [
    (1, 20114.9),
    (5, 20116.48),
    (10, 20127.38)
])
def test_good_values(candles, expected_result):
    assert ema(candles, OHLC) == expected_result


def test_zero_candles():
    with pytest.raises(ValueError):
        ema(0, OHLC)


def test_negative_candles():
    with pytest.raises(ValueError):
        ema(-1, OHLC)


@pytest.mark.parametrize("candles", [
    ("10"),
    ([10, 11]),
    ({"SMA": 12}),
])
def test_type_candles(candles):
    with pytest.raises(TypeError):
        ema(candles, OHLC)
