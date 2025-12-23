import pandas as pd
import numpy as np
import pytest

from engine.indicators import calculate_rsi, calculate_vwap, calculate_atr


@pytest.fixture
def sample_ohlcv():
    """
    Deterministic OHLCV data for testing indicators.
    30 rows ensures RSI/ATR (period=14) can produce values.
    """
    data = {
        "open":   np.arange(100, 130),
        "high":   np.arange(101, 131),
        "low":    np.arange(99, 129),
        "close":  np.arange(100, 130),
        "volume": np.arange(1000, 4000, 100),
    }
    return pd.DataFrame(data)


def test_vwap_returns_series_same_length(sample_ohlcv):
    vwap = calculate_vwap(sample_ohlcv)
    assert isinstance(vwap, pd.Series)
    assert len(vwap) == len(sample_ohlcv)


def test_vwap_has_no_nans(sample_ohlcv):
    vwap = calculate_vwap(sample_ohlcv)
    assert vwap.isna().sum() == 0


def test_rsi_returns_series_same_length(sample_ohlcv):
    rsi = calculate_rsi(sample_ohlcv, period=14)
    assert isinstance(rsi, pd.Series)
    assert len(rsi) == len(sample_ohlcv)


def test_rsi_bounds(sample_ohlcv):
    rsi = calculate_rsi(sample_ohlcv, period=14)
    valid = rsi.dropna()
    assert (valid >= 0).all()
    assert (valid <= 100).all()


def test_rsi_has_nans_for_insufficient_data():
    short_df = pd.DataFrame({
        "close": np.arange(1, 10)
    })
    rsi = calculate_rsi(short_df, period=14)
    assert rsi.isna().all()


def test_atr_returns_series_same_length(sample_ohlcv):
    atr = calculate_atr(sample_ohlcv, period=14)
    assert isinstance(atr, pd.Series)
    assert len(atr) == len(sample_ohlcv)


def test_atr_non_negative(sample_ohlcv):
    atr = calculate_atr(sample_ohlcv, period=14)
    valid = atr.dropna()
    assert (valid >= 0).all()


def test_atr_has_nans_for_insufficient_data():
    short_df = pd.DataFrame({
        "high":  np.arange(1, 10),
        "low":   np.arange(0, 9),
        "close": np.arange(1, 10),
    })
    atr = calculate_atr(short_df, period=14)
    assert atr.isna().all()
