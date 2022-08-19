from fastapi import APIRouter
from models.schemas import Interval

router = APIRouter()

@router.get("/sma/")
async def get_ma(interval: Interval, symbol: str):
    # some magic calculations
    value = 50
    return {"value": value}