from fastapi import APIRouter, Query, HTTPException
from models.schemas import Interval
from utils.indicators.ema import ema
from utils.get_OHLC import kraken_OHLC

router = APIRouter()


@router.get("/ema")
async def get_ema(interval: Interval, symbol: str, candles: int = Query(default=50)):
    try:
        return {"value": ema(candles, kraken_OHLC(symbol, interval))}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
