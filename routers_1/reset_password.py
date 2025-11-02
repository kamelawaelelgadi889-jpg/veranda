
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import hashlib

from database import get_db
from models.user import User
from schemas import ResetPasswordRequest

router = APIRouter()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

@router.post("/reset-password/{token}")
def reset_password(token: str, request: ResetPasswordRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.reset_token == token).first()

    if not user:
        raise HTTPException(status_code=404, detail="المستخدم غير موجود")
    if user.token_expiration < datetime.utcnow():
        raise HTTPException(status_code=400, detail="الرابط منتهي الصلاحية")

    user.password_hash = hash_password(request.new_password)
    user.reset_token = None
    user.token_expiration = None
    db.commit()

    return {"message": "تم تغيير كلمة المرور بنجاح"}