from pydantic import BaseModel, validator
from enum import Enum

class Interval(str, Enum):
    one_m = "1m", 
    five_m = "5m", 
    fifteen_m = "15m", 
    thirty_m = "30m", 
    one_hour = "1h", 
    two_hour = "2h", 
    four_hour = "4h", 
    twelve_hour = "12h",
    one_day = "1d",
    one_week = "1w"

