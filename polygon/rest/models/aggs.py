from typing import Optional
from ...modelclass import modelclass


@modelclass
class Agg:
    "Contains aggregate data for a given ticker symbol over a given date range in a custom time window size."
    open: Optional[float] = -999
    high: Optional[float] = -999
    low: Optional[float] = -999
    close: Optional[float] = -999
    volume: Optional[float] = -999
    vwap: Optional[float] = -999
    timestamp: Optional[int] = 0
    transactions: Optional[int] = -999
    otc: Optional[bool] = False

    @staticmethod
    def from_dict(d):
        return Agg(
            d.get("o", -999),
            d.get("h", -999),
            d.get("l", -999),
            d.get("c", -999),
            d.get("v", -999),
            d.get("vw", -999),
            d.get("t", 0),
            d.get("n", -999),
            d.get("otc", False),
        )


@modelclass
class GroupedDailyAgg:
    "Contains daily open, high, low, and close (OHLC) data for a given date."
    ticker: Optional[str] = None
    open: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    close: Optional[float] = None
    volume: Optional[float] = None
    vwap: Optional[float] = None
    timestamp: Optional[int] = None
    transactions: Optional[int] = None
    otc: Optional[bool] = None

    @staticmethod
    def from_dict(d):
        return GroupedDailyAgg(
            d.get("T", None),
            d.get("o", None),
            d.get("h", None),
            d.get("l", None),
            d.get("c", None),
            d.get("v", None),
            d.get("vw", None),
            d.get("t", None),
            d.get("n", None),
            d.get("otc", None),
        )


@modelclass
class DailyOpenCloseAgg:
    "Contains data for open, close and afterhours prices of a ticker symbol on a specified date."
    after_hours: Optional[float] = None
    close: Optional[float] = None
    from_: Optional[str] = None
    high: Optional[float] = None
    low: Optional[float] = None
    open: Optional[float] = None
    pre_market: Optional[float] = None
    status: Optional[str] = None
    symbol: Optional[str] = None
    volume: Optional[float] = None
    otc: Optional[bool] = None

    @staticmethod
    def from_dict(d):
        return DailyOpenCloseAgg(
            d.get("afterHours", None),
            d.get("close", None),
            d.get("from", None),
            d.get("high", None),
            d.get("low", None),
            d.get("open", None),
            d.get("preMarket", None),
            d.get("status", None),
            d.get("symbol", None),
            d.get("volume", None),
            d.get("otc", None),
        )


@modelclass
class PreviousCloseAgg:
    "Contains data for the previous day's open, high, low, and close (OHLC) of the specified stock ticker."
    ticker: Optional[str] = None
    close: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    open: Optional[float] = None
    timestamp: Optional[float] = None
    volume: Optional[float] = None
    vwap: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return PreviousCloseAgg(
            d.get("T", None),
            d.get("c", None),
            d.get("h", None),
            d.get("l", None),
            d.get("o", None),
            d.get("t", None),
            d.get("v", None),
            d.get("vw", None),
        )
