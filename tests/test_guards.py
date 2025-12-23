import pandas as pd
from datetime import datetime, time
import pytz

from engine.guards import is_market_open, has_min_rows, apply_nan_policy


def test_market_open_true():
    now = pytz.timezone("Asia/Kolkata").localize(datetime(2024, 1, 1, 10, 0))
    assert is_market_open(now, time(9, 15), time(15, 30), "Asia/Kolkata")


def test_market_open_false():
    now = pytz.timezone("Asia/Kolkata").localize(datetime(2024, 1, 1, 8, 0))
    assert not is_market_open(now, time(9, 15), time(15, 30), "Asia/Kolkata")


def test_min_rows():
    df = pd.DataFrame({"a": range(10)})
    assert not has_min_rows(df, 20)
    assert has_min_rows(df, 5)


def test_nan_policy_zero():
    s = pd.Series([1, None, 3])
    out = apply_nan_policy(s, "zero")
    assert out.isna().sum() == 0
