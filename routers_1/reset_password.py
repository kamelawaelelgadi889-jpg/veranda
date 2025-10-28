from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from models.user import User
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime
import hashlib
from schemas import ResetRequest

router = APIRouter()



def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

@router.post("/reset-password/{token}")
def reset_password(token: str, request: ResetRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.reset_token == token).first()
    if not user or user.token_expiration < datetime.utcnow():
        raise HTTPException(status_code=400, detail="الرابط غير صالح أو منتهي")

    user.password_hash = hash_password(request.new_password)
    user.reset_token = None
    user.token_expiration = None
    db.commit()

    return {"message": "تم تغيير كلمة المرور بنجاح"}