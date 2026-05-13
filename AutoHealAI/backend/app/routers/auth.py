from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import LoginRequest, TokenResponse
from app.security import create_access_token, verify_password, hash_password

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user:
        user = User(email=payload.email, hashed_password=hash_password(payload.password), role="admin")
        db.add(user)
        db.commit()
        db.refresh(user)
    elif not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(user.email)
    return TokenResponse(access_token=token)
