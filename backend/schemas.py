from pydantic import BaseModel
from typing import Dict, Any, List


class HealthResponse(BaseModel):
    status: str


class MetricsResponse(BaseModel):
    metrics: Dict[str, Any]


class ScoreResponse(BaseModel):
    score: List[float]
