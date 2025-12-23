import pandas as pd
from datetime import datetime, time
import pytz


def is_market_open(
    now: datetime,
    market_open: time,
    market_close: time,
    timezone: str
) -> bool:
    tz = pytz.timezone(timezone)
    local_time = now.astimezone(tz).time()
    return market_open <= local_time <= market_close


def has_min_rows(df: pd.DataFrame, min_rows: int) -> bool:
    return len(df) >= min_rows


def apply_nan_policy(
    series: pd.Series,
    policy: str = "ignore"
) -> pd.Series:
    if policy == "ignore":
        return series
    if policy == "zero":
        return series.fillna(0)
    if policy == "drop":
        return series.dropna()
    raise ValueError(f"Unknown NaN policy: {policy}")
