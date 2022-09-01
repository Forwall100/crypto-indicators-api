from enum import Enum

class Interval(str, Enum):
    one_m = "1m", 
    five_m = "5m", 
    fifteen_m = "15m", 
    thirty_m = "30m", 
    one_hour = "1h", 
    four_hour = "4h", 
    one_day = "1d",
    one_week = "1w"

