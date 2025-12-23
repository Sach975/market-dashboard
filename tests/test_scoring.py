import pandas as pd
import numpy as np

from engine.scoring import calculate_score


def sample_metrics():
    idx = pd.RangeIndex(5)

    return {
        "volume_spike": pd.Series([1.0, 3.0, 2.6, 1.2, 4.0], index=idx),
        "vwap_position": pd.Series([-0.1, 0.2, 0.1, -0.05, 0.3], index=idx),
        "rsi_regime": pd.Series(
            ["neutral", "bullish", "bullish", "oversold", "overextended"],
            index=idx
        ),
        "breakout": {
            "bullish_breakout": pd.Series([0, 1, 0, 0, 1], index=idx),
            "bearish_breakdown": pd.Series([0, 0, 0, 1, 0], index=idx),
        },
        "atr_expansion": pd.Series([False, True, True, False, True], index=idx),
    }


def sample_config():
    return {
        "volume_spike": {"min_ratio": 2.5, "weight": 3},
        "vwap_position": {"above": 0.0, "weight": 2},
        "rsi_regime": {
            "bullish": 2,
            "neutral": 0,
            "oversold": 1,
            "overextended": -2,
        },
        "breakout": {"bullish": 3, "bearish": -3},
        "atr_expansion": {"enabled": True, "weight": 1},
    }


def test_score_shape():
    score = calculate_score(sample_metrics(), sample_config())
    assert isinstance(score, pd.Series)
    assert len(score) == 5


def test_score_changes_with_metrics():
    score = calculate_score(sample_metrics(), sample_config())
    assert score.iloc[1] > score.iloc[0]


def test_negative_score_possible():
    score = calculate_score(sample_metrics(), sample_config())
    assert (score < 0).any()
