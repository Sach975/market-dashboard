from fastapi import FastAPI

from backend.schemas import HealthResponse, MetricsResponse, ScoreResponse
from backend.services import load_sample_data, compute_metrics, compute_score

app = FastAPI(title="Market Dashboard API", version="1.0")


@app.get("/health", response_model=HealthResponse)
def health():
    return {"status": "ok"}


@app.get("/metrics", response_model=MetricsResponse)
def metrics():
    df = load_sample_data()
    metrics = compute_metrics(df)
    # Convert series to JSON-safe
    return {
        "metrics": {
            k: (
                {kk: vv.tolist() for kk, vv in v.items()}
                if isinstance(v, dict)
                else v.tolist()
            )
            for k, v in metrics.items()
        }
    }


@app.get("/score", response_model=ScoreResponse)
def score():
    df = load_sample_data()
    score_series = compute_score(df)
    return {"score": score_series.tolist()}
