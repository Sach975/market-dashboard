# Project Design Document

## Objective
Build a real-time stock analysis dashboard that computes short-term trading
metrics using deterministic, rule-based mathematical logic to assist
manual trading decisions.

---

## What This Project Does
- Fetches near-real-time price and volume data for selected stocks
- Computes short-term technical indicators and derived metrics
- Maps metrics to a structured checklist and composite score
- Presents all information in a single, low-latency interface
- Acts strictly as a decision-support tool

---

## What This Project Does NOT Do
- Does not predict future stock prices
- Does not execute or automate trades
- Does not use machine learning or artificial intelligence
- Does not provide financial advice or guarantees
- Does not optimize or suggest position sizing

---

## Target Market & Use Case
- Market: Indian equities (NSE)
- Time horizon: Short-term (intraday to few days)
- Trading style: Momentum and event-driven price spikes
- Capital usage: Small, disposable capital
- User type: Retail trader seeking structured real-time information

---

## Decision Philosophy
This system is designed to enhance situational awareness, not to replace
human judgment.

All outputs are descriptive rather than prescriptive. The user is expected
to:
- Interpret metrics contextually
- Apply independent risk management
- Decide entries and exits manually

---

## Metrics Used (Initial Scope)
The following metrics will be implemented in the initial version:
- Relative Strength Index (RSI)
- Volume Weighted Average Price (VWAP)
- Average True Range (ATR)
- Volume Spike Ratio
- Short-term High/Low Breakout detection

These metrics are chosen for their relevance to short-term momentum and
volatility analysis.

---

## Scoring Philosophy
Metrics contribute positively or negatively to a composite
"Spike Readiness Score".

The score is intended to:
- Highlight favorable short-term trading conditions
- Penalize excessive risk or poor liquidity
- Remain interpretable and rule-based

No metric independently determines trade decisions.

---

## Known Limitations
- Market data latency depends on third-party data providers
- Sudden news-driven moves may occur before indicators update
- Indicators are inherently lagging during rapid reversals
- The system is not suitable for long-term investment analysis

---

## Future Extensions (Out of Scope for Initial Version)
- Automated news sentiment analysis
- Backtesting and performance analytics
- Strategy automation or order execution
- Machine learning-based signal generation
