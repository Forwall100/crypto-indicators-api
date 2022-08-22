from typing import Optional
from fastapi import APIRouter
from models.schemas import Interval
from utils.sma import sma

router = APIRouter()

@router.get("/sma{candles}/")
async def get_ma(interval: Interval, symbol: str, candles: int):
    try:
        return {"value": sma(interval, candles, symbol)}
    except ValueError:
        return {"Unknown pair"}