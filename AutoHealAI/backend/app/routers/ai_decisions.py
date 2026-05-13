from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import RemediationAction

router = APIRouter()


@router.get("/")
def decisions(db: Session = Depends(get_db)):
    return db.query(RemediationAction).order_by(RemediationAction.executed_at.desc()).limit(100).all()
