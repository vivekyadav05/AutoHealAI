from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import DeploymentHistory

router = APIRouter()


@router.post("/risk-analysis")
def deployment_risk_analysis(service: str, version: str, risk_score: float, db: Session = Depends(get_db)):
    unstable = risk_score >= 0.75
    entry = DeploymentHistory(
        service=service,
        version=version,
        deployed_by="autohealai-agent",
        risk_score=risk_score,
        is_rolled_back=unstable,
    )
    db.add(entry)
    db.commit()
    return {
        "service": service,
        "version": version,
        "risk_score": risk_score,
        "rollback_triggered": unstable,
        "message": "Automatic rollback initiated." if unstable else "Deployment stable.",
    }
