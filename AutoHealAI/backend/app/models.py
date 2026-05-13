from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean

from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(50), default="viewer")
    created_at = Column(DateTime, default=datetime.utcnow)


class Metric(Base):
    __tablename__ = "metrics"
    id = Column(Integer, primary_key=True)
    service = Column(String(128), index=True)
    cpu = Column(Float, nullable=False)
    memory = Column(Float, nullable=False)
    latency = Column(Float, nullable=False)
    error_rate = Column(Float, nullable=False)
    restarts = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)


class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True)
    service = Column(String(128), index=True)
    failure_probability = Column(Float, nullable=False)
    severity = Column(String(32), nullable=False)
    confidence = Column(Float, nullable=False)
    recommendation = Column(Text, nullable=False)
    model_version = Column(String(64), default="v1")
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)


class Incident(Base):
    __tablename__ = "incidents"
    id = Column(Integer, primary_key=True)
    service = Column(String(128), index=True)
    status = Column(String(32), default="open")
    root_cause = Column(Text, nullable=False)
    detected_at = Column(DateTime, default=datetime.utcnow)
    resolved_at = Column(DateTime, nullable=True)


class RemediationAction(Base):
    __tablename__ = "remediation_actions"
    id = Column(Integer, primary_key=True)
    incident_id = Column(Integer, nullable=True)
    service = Column(String(128), index=True)
    action_type = Column(String(64), nullable=False)
    status = Column(String(32), default="queued")
    explanation = Column(Text, nullable=False)
    executed_at = Column(DateTime, default=datetime.utcnow)


class DeploymentHistory(Base):
    __tablename__ = "deployment_history"
    id = Column(Integer, primary_key=True)
    service = Column(String(128), index=True)
    version = Column(String(64), nullable=False)
    deployed_by = Column(String(128), nullable=False)
    risk_score = Column(Float, default=0.0)
    is_rolled_back = Column(Boolean, default=False)
    deployed_at = Column(DateTime, default=datetime.utcnow)


class LogEntry(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True)
    service = Column(String(128), index=True)
    level = Column(String(16), nullable=False)
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
