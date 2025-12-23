import pandas as pd
from pathlib import Path

from engine.indicators import calculate_rsi, calculate_vwap, calculate_atr
from engine.metrics import (
    volume_spike_ratio,
    breakout_flags,
    vwap_position,
    rsi_regime,
    atr_expansion,
)
from engine.scoring import calculate_score, load_scoring_config


DATA_PATH = Path("data/samples/sample_ohlc.csv")
SCORING_CONFIG_PATH = Path("config/scoring.yaml")


def load_sample_data() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)


def compute_metrics(df: pd.DataFrame) -> dict:
    rsi = calculate_rsi(df)
    vwap = calculate_vwap(df)
    atr = calculate_atr(df)

    return {
        "volume_spike": volume_spike_ratio(df),
        "vwap_position": vwap_position(df["close"], vwap),
        "rsi_regime": rsi_regime(rsi),
        "breakout": breakout_flags(df),
        "atr_expansion": atr_expansion(atr),
    }


def compute_score(df: pd.DataFrame) -> pd.Series:
    metrics = compute_metrics(df)
    config = load_scoring_config(SCORING_CONFIG_PATH)
    return calculate_score(metrics, config)
