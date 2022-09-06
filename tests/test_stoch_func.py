from utils.indicators.stoch import stoch
from .OHLC_test_data import OHLC
import pytest


@pytest.mark.parametrize("k_period, d_period, expected_result", [
    (1, 2, [6.95, 3.48]),
    (5, 4, [71.4, 67.95]),
    (6, 3, [53.35, 54.89])
])
def test_good_values(k_period, d_period, expected_result):
    assert stoch(k_period, d_period, OHLC) == expected_result


@pytest.mark.parametrize("k_period, d_period", [
    (0, 5),
    (5, 0)
])
def test_zero_periods(k_period, d_period):
    with pytest.raises(ValueError):
        stoch(k_period, d_period, OHLC)


@pytest.mark.parametrize("k_period, d_period", [
    (-1, 5),
    (5, -1)
])
def test_negative_periods(k_period, d_period):
    with pytest.raises(ValueError):
        stoch(k_period, d_period, OHLC)


@pytest.mark.parametrize("k_period, d_period", [
    ("10", 5),
    ([10, 11], 3),
    ({"STOCH": 12}, 1),
    (5, "10"),
    (3, [10, 11]),
    (1, {"STOCH": 1})
])
def test_type_periods(k_period, d_period):
    with pytest.raises(TypeError):
        stoch(k_period, d_period, OHLC)
