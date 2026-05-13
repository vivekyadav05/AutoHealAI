from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Incident

router = APIRouter()


@router.get("/")
def list_incidents(db: Session = Depends(get_db)):
    return db.query(Incident).order_by(Incident.detected_at.desc()).limit(100).all()
