from fastapi import APIRouter, Query
from models.schemas import Interval
from utils.indicators.rsi import rsi
from utils.get_OHLC import kraken_OHLC

router = APIRouter()

@router.get("/rsi")
async def get_rsi(interval: Interval, symbol: str, candles: int = Query(default=14)):
    try:
        return {"value": rsi(candles, kraken_OHLC(symbol, interval))}
    except ValueError:
        return {"Unknown pair"}