from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Metric, Prediction, RemediationAction
from app.schemas import MetricIn, MetricOut
from app.services.predictor import predict_failure
from app.services.remediator import get_remediation_plan

router = APIRouter()


@router.post("/ingest", response_model=MetricOut)
def ingest_metric(payload: MetricIn, db: Session = Depends(get_db)):
    metric = Metric(**payload.model_dump())
    db.add(metric)
    db.commit()
    db.refresh(metric)

    prob, severity, confidence, recommendation = predict_failure(
        payload.cpu, payload.memory, payload.latency, payload.error_rate, payload.restarts
    )

    pred = Prediction(
        service=payload.service,
        failure_probability=prob,
        severity=severity,
        confidence=confidence,
        recommendation=recommendation,
    )
    db.add(pred)

    if severity in ("critical", "high"):
        plan = get_remediation_plan(payload.service, severity)
        action = RemediationAction(service=payload.service, **plan)
        db.add(action)

    db.commit()
    return metric


@router.get("/latest", response_model=list[MetricOut])
def latest_metrics(db: Session = Depends(get_db)):
    return db.query(Metric).order_by(Metric.timestamp.desc()).limit(50).all()
