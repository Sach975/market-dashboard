import yaml
import pandas as pd
from typing import Dict


def load_scoring_config(path: str) -> Dict:
    """
    Load scoring configuration from YAML.
    """
    with open(path, "r") as f:
        return yaml.safe_load(f)


def calculate_score(
    metrics: Dict[str, pd.Series | Dict[str, pd.Series]],
    config: Dict
) -> pd.Series:
    """
    Compute composite score from metric inputs.

    metrics keys expected:
    - volume_spike (pd.Series)
    - vwap_position (pd.Series)
    - rsi_regime (pd.Series)
    - breakout (dict of pd.Series)
    - atr_expansion (pd.Series)
    """
    # Use index from any metric
    index = next(iter(metrics.values()))
    if isinstance(index, dict):
        index = next(iter(index.values()))
    score = pd.Series(0, index=index.index)

    # Volume spike
    vol_ratio = metrics["volume_spike"]
    score += (vol_ratio >= config["volume_spike"]["min_ratio"]) * config["volume_spike"]["weight"]

    # VWAP position
    vwap_pos = metrics["vwap_position"]
    score += (vwap_pos > config["vwap_position"]["above"]) * config["vwap_position"]["weight"]

    # RSI regime
    rsi_regime = metrics["rsi_regime"]
    for regime, weight in config["rsi_regime"].items():
        score += (rsi_regime == regime) * weight

    # Breakouts
    breakout = metrics["breakout"]
    score += breakout["bullish_breakout"] * config["breakout"]["bullish"]
    score += breakout["bearish_breakdown"] * config["breakout"]["bearish"]

    # ATR expansion
    if config["atr_expansion"]["enabled"]:
        score += metrics["atr_expansion"] * config["atr_expansion"]["weight"]

    # Ensure score has no NaNs
    score = score.fillna(0)
    return score

