from fastapi import APIRouter, Query
from models.schemas import Interval
from utils.sma import sma

router = APIRouter()

@router.get("/sma")
async def get_ma(interval: Interval, symbol: str, candles: int = Query(default=50)):
    try:
        return {"value": sma(interval, candles, symbol)}
    except ValueError:
        return {"Unknown pair"}