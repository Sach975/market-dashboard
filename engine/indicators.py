import pandas as pd
import numpy as np


def calculate_vwap(df: pd.DataFrame) -> pd.Series:
    required_cols = {"close", "volume"}
    if not required_cols.issubset(df.columns):
        raise ValueError("DataFrame must contain 'close' and 'volume' columns")

    cumulative_price_volume = (df["close"] * df["volume"]).cumsum()
    cumulative_volume = df["volume"].cumsum()
    return cumulative_price_volume / cumulative_volume


def calculate_rsi(df: pd.DataFrame, period: int = 14) -> pd.Series:
    if "close" not in df.columns:
        raise ValueError("DataFrame must contain 'close' column")

    delta = df["close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(alpha=1/period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/period, min_periods=period, adjust=False).mean()

    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def calculate_atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
    required_cols = {"high", "low", "close"}
    if not required_cols.issubset(df.columns):
        raise ValueError("DataFrame must contain 'high', 'low', and 'close' columns")

    high = df["high"]
    low = df["low"]
    close = df["close"]
    prev_close = close.shift(1)

    tr = pd.concat(
        [
            high - low,
            (high - prev_close).abs(),
            (low - prev_close).abs(),
        ],
        axis=1,
    ).max(axis=1)

    return tr.ewm(alpha=1/period, min_periods=period, adjust=False).mean()
