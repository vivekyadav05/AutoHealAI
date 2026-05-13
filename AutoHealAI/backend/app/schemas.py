from datetime import datetime
from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class MetricIn(BaseModel):
    service: str
    cpu: float
    memory: float
    latency: float
    error_rate: float
    restarts: int


class MetricOut(MetricIn):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True


class PredictionOut(BaseModel):
    id: int
    service: str
    failure_probability: float
    severity: str
    confidence: float
    recommendation: str
    model_version: str
    timestamp: datetime

    class Config:
        from_attributes = True
