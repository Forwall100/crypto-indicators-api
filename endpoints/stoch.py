from fastapi import APIRouter, Query, HTTPException
from models.schemas import Interval
from utils.indicators.stoch import stoch
from utils.get_OHLC import kraken_OHLC

router = APIRouter()


@router.get("/stoch")
async def get_stoch(interval: Interval, symbol: str, k_period: int = Query(default=5), d_period: int = Query(default=3),):
    result = stoch(k_period, d_period, kraken_OHLC(symbol, interval))
    try:
        return {
            "value%K": result[0],
            "value%D": result[1]
        }
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
