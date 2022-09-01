from fastapi import APIRouter, Query
from models.schemas import Interval
from utils.indicators.rsi import rsi

router = APIRouter()

@router.get("/rsi")
async def get_rsi(interval: Interval, symbol: str, candles: int = Query(default=14)):
    try:
        return {"value": rsi(interval, candles, symbol)}
    except ValueError:
        return {"Unknown pair"}