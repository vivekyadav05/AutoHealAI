from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import get_current_user
from app.models import Prediction
from app.schemas import PredictionOut

router = APIRouter()


@router.get("/", response_model=list[PredictionOut])
def list_predictions(db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    return db.query(Prediction).order_by(Prediction.timestamp.desc()).limit(100).all()
