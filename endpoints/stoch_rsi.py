from fastapi import APIRouter, Query, HTTPException
from models.schemas import Interval
from utils.indicators.stoch_rsi import stoch_rsi
from utils.get_OHLC import kraken_OHLC

router = APIRouter()


@router.get("/stochrsi")
async def get_stoch_rsi(interval: Interval, symbol: str, candles: int = Query(default=14)):
    try:
        return {"value": stoch_rsi(candles, kraken_OHLC(symbol, interval))}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
