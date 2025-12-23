import pandas as pd
from typing import Dict

def volume_spike_ratio(
    df: pd.DataFrame,
    window: int = 20
) -> pd.Series:
    """
    Ratio of current volume to rolling average volume.
    """
    if "volume" not in df.columns:
        raise ValueError("DataFrame must contain 'volume' column")

    avg_volume = df["volume"].rolling(window=window).mean()
    return df["volume"] / avg_volume

def breakout_flags(
    df: pd.DataFrame,
    window: int = 20
) -> Dict[str, pd.Series]:
    """
    Detect short-term bullish or bearish breakouts.
    """
    if not {"high", "low", "close"}.issubset(df.columns):
        raise ValueError("DataFrame must contain 'high', 'low', 'close'")

    rolling_high = df["high"].rolling(window=window).max()
    rolling_low = df["low"].rolling(window=window).min()

    bullish = df["close"] > rolling_high.shift(1)
    bearish = df["close"] < rolling_low.shift(1)

    return {
        "bullish_breakout": bullish,
        "bearish_breakdown": bearish,
    }

def vwap_position(
    price: pd.Series,
    vwap: pd.Series
) -> pd.Series:
    """
    Position of price relative to VWAP.
    """
    return (price - vwap) / vwap

def rsi_regime(
    rsi: pd.Series
) -> pd.Series:
    """
    Classify RSI into regimes.
    """
    regime = pd.Series(index=rsi.index, dtype="object")

    regime[rsi < 30] = "oversold"
    regime[(rsi >= 30) & (rsi < 55)] = "neutral"
    regime[(rsi >= 55) & (rsi <= 70)] = "bullish"
    regime[rsi > 70] = "overextended"

    return regime

def atr_expansion(
    atr: pd.Series,
    window: int = 5
) -> pd.Series:
    """
    Detect whether ATR is expanding relative to recent average.
    """
    atr_avg = atr.rolling(window=window).mean()
    return atr > atr_avg
