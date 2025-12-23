import pandas as pd
import numpy as np

from engine.metrics import (
    volume_spike_ratio,
    breakout_flags,
    vwap_position,
    rsi_regime,
    atr_expansion,
)


def sample_df():
    return pd.DataFrame({
        "open":   np.arange(100, 140),
        "high":   np.arange(101, 141),
        "low":    np.arange(99, 139),
        "close":  np.arange(100, 140),
        "volume": np.linspace(1000, 4000, 40),
    })


def test_volume_spike_ratio_shape():
    df = sample_df()
    ratio = volume_spike_ratio(df)
    assert len(ratio) == len(df)


def test_breakout_flags_keys():
    df = sample_df()
    flags = breakout_flags(df)
    assert "bullish_breakout" in flags
    assert "bearish_breakdown" in flags


def test_vwap_position_zero_when_equal():
    price = pd.Series([100, 100])
    vwap = pd.Series([100, 100])
    pos = vwap_position(price, vwap)
    assert (pos == 0).all()


def test_rsi_regime_labels():
    rsi = pd.Series([20, 40, 60, 80])
    regime = rsi_regime(rsi)
    assert list(regime) == ["oversold", "neutral", "bullish", "overextended"]


def test_atr_expansion_shape():
    atr = pd.Series(np.arange(1, 30))
    expanded = atr_expansion(atr)
    assert len(expanded) == len(atr)
