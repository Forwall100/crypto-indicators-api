from fastapi import APIRouter, Query, HTTPException
from models.schemas import Interval
from utils.indicators.sma import sma
from utils.get_OHLC import kraken_OHLC

router = APIRouter()


@router.get("/sma")
async def get_sma(interval: Interval, symbol: str, candles: int = Query(default=50)):
    try:
        return {"value": sma(candles, kraken_OHLC(symbol, interval))}
    except ZeroDivisionError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
