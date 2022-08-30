from fastapi import APIRouter, Query
from models.schemas import Interval
from utils.ema import ema

router = APIRouter()

@router.get("/ema")
async def get_ema(interval: Interval, symbol: str, candles: int = Query(default=50)):
    try:
        return {"value": ema(interval, candles, symbol)}
    except ValueError:
        return {"Unknown pair"}