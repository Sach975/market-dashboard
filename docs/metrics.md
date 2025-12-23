# Metric Specifications (v1)

This document defines the core metrics used in the initial version of the
short-term stock analysis system. All metrics are deterministic, rule-based,
and designed to support manual trading decisions.

The metrics selected here are intentionally minimal and non-redundant.

---

## 1. Relative Strength Index (RSI)

**Purpose**  
Measure short-term momentum to identify whether price movement is strengthening
or becoming overextended.

**Inputs**  
- Close prices
- Intraday OHLC candles

**Calculation**  
RSI is computed using Wilder’s smoothing method:
- Calculate average gains and losses over N periods
- RS = Average Gain / Average Loss
- RSI = 100 − (100 / (1 + RS))

**Parameters**  
- Lookback period: 14
- Timeframe: Intraday candles (e.g., 5m or 15m)

**Interpretation**  
- RSI < 30: Oversold conditions  
- RSI 55–70: Healthy bullish momentum  
- RSI > 75: Overextended, higher pullback risk  

**Edge Cases**  
- RSI can remain overbought during strong trends  
- Less reliable during low-liquidity periods  

---

## 2. Volume Weighted Average Price (VWAP)

**Purpose**  
Identify the intraday average traded price weighted by volume to assess
institutional bias and trend control.

**Inputs**  
- Price (close or typical price)
- Volume

**Calculation**  
VWAP = Σ(Price × Volume) / Σ(Volume)

**Parameters**  
- Reset at the start of each trading day  
- Calculated intraday only  

**Interpretation**  
- Price above VWAP: Bullish intraday bias  
- Price below VWAP: Bearish intraday bias  
- Strong moves away from VWAP indicate momentum  

**Edge Cases**  
- VWAP becomes less informative late in the trading session  
- Not suitable for multi-day analysis  

---

## 3. Average True Range (ATR)

**Purpose**  
Measure short-term volatility to estimate movement potential and risk.

**Inputs**  
- High, Low, Close prices

**Calculation**  
True Range (TR) is defined as the maximum of:
- High − Low  
- |High − Previous Close|  
- |Low − Previous Close|  

ATR is the moving average of TR over N periods using Wilder’s smoothing.

**Parameters**  
- Lookback period: 14  
- Timeframe aligned with RSI  

**Interpretation**  
- Rising ATR: Expanding volatility  
- Falling ATR: Volatility compression (potential breakout setup)  

**Edge Cases**  
- ATR does not indicate direction  
- Sudden news events can invalidate ATR expectations  

---

## 4. Volume Spike Ratio

**Purpose**  
Detect abnormal trading activity that may indicate increased market
participation or reaction to news.

**Inputs**  
- Current candle volume  
- Historical average volume  

**Calculation**  
Volume Spike Ratio = Current Volume / Average Volume

**Parameters**  
- Average volume lookback: 20 periods  
- Timeframe aligned with other metrics  

**Interpretation**  
- Ratio ≥ 2.5: Significant volume expansion  
- Ratio ≥ 4.0: Exceptional activity  

**Edge Cases**  
- Can spike on illiquid stocks  
- Requires liquidity filtering elsewhere  

---

## 5. Short-Term High/Low Breakout

**Purpose**  
Identify momentum continuation through recent price extremes.

**Inputs**  
- High and Low prices

**Calculation**  
- Bullish breakout: Current price > Highest High of last N periods  
- Bearish breakdown: Current price < Lowest Low of last N periods  

**Parameters**  
- Lookback window: 20 periods  

**Interpretation**  
- Breakout with volume confirmation strengthens conviction  
- False breakouts common without volume confirmation  

**Edge Cases**  
- Prone to whipsaws in range-bound markets  

---

## Metrics Explicitly Out of Scope (v1)

The following metrics are intentionally excluded to avoid redundancy and
overfitting in the initial version:

- MACD  
- Bollinger Bands  
- Stochastic Oscillator  
- ADX  
- Ichimoku Cloud  
- Fibonacci-based indicators  

These may be evaluated in future versions if justified by clear use cases.

---

## Versioning

This document defines **Metric Specifications v1**.
Any additions or changes must be documented in a new versioned specification.
