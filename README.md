# Market Dashboard

A rule-based, short-term stock analysis dashboard designed to provide
structured, real-time market insights using deterministic metrics and
transparent scoring logic.

This project is NOT a trading bot and does NOT make predictions.
It is a decision-support system intended to assist manual analysis.

---

## 🚀 Features

- Technical indicator engine (RSI, VWAP, ATR)
- Interpretable metrics layer (volume spikes, breakouts, regimes)
- Config-driven scoring engine (no hardcoded logic)
- Automated test coverage using pytest
- FastAPI backend with documented endpoints
- Minimal, read-only frontend dashboard
- Clean separation of concerns (engine, backend, frontend)

---

## 🧠 Design Philosophy

- No AI / Machine Learning
- No automated trading or execution
- No price prediction
- Deterministic and explainable logic
- Rule-based and configurable
- Built for clarity, extensibility, and correctness

This project prioritizes engineering discipline and interpretability
over complexity.

For full design intent, scope, and architectural decisions, see:
PROJECT.md

---

## 🏗️ Project Structure

engine/        -> Core logic (indicators, metrics, scoring)  
backend/       -> FastAPI service  
frontend/      -> Minimal dashboard UI  
config/        -> YAML-based configuration  
tests/         -> Automated tests  
docs/          -> Metric specifications  
data/          -> Sample OHLCV data  

---

## ▶️ Getting Started

1. Install dependencies

pip install -r requirements.txt

2. Start the backend API

uvicorn backend.main:app --reload

The backend will be available at:
http://127.0.0.1:8000

3. Open the frontend dashboard

Open the following file in your browser:
frontend/index.html

---

## 🔍 API Endpoints

/health   -> Service health check  
/metrics  -> Computed metrics  
/score    -> Composite score  
/docs     -> Interactive API documentation (Swagger UI)

---

## 🧪 Running Tests

pytest

All core logic is covered by automated tests.

---

## ⚠️ Disclaimer

This project is for educational and analytical purposes only.

It does NOT provide financial advice, investment recommendations,
or guarantees of profitability.

All trading decisions and risk management remain the responsibility
of the user.

---

## 📌 Status

Core engine complete  
Backend API complete  
Frontend dashboard complete  

Future extensions may include:
- Live market data integration
- Charting
- Backtesting
- Deployment
- Optional AI experimentation (separate module)

---

## 👤 Author

Built as a professional-grade engineering project focused on
financial systems, software architecture, and deterministic analysis.
