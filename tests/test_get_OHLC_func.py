from typing import Type
from utils.get_OHLC import kraken_OHLC
import pytest
from utils.constans import intervals


def test_bad_pair():
    with pytest.raises(ValueError):
        kraken_OHLC("BADPAIR", intervals["1m"])


def test_bad_interval():
    with pytest.raises(ValueError):
        kraken_OHLC("BTCUSD", 13370)


@pytest.mark.parametrize("pair, interval", [
    (123, intervals["1m"]),
    ({"BTCUSD": 1}, intervals["1m"]),
    (["BTCUSD"], intervals["1m"]),
    (True, intervals["1m"])
])
def test_type_pair(pair, interval):
    with pytest.raises(ValueError):
        kraken_OHLC(pair, interval)


@pytest.mark.parametrize("pair, interval", [
    ("BTCUSD", "1m"),
    ("BTCUSD", ["1m"]),
    ("BTCUSD", {1: "1m"}),
    ("BTCUSD", True)
])
def test_type_interval(pair, interval):
    with pytest.raises(ValueError):
        kraken_OHLC(pair, interval)
