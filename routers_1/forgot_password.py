
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import secrets
from pydantic import BaseModel
from typing import Optional

from database import get_db
from models.user import User

router = APIRouter()

class ForgotPasswordRequest(BaseModel):
    email: Optional[str] = None
    phone_number: Optional[str] = None

@router.post("/forgot-password")
def forgot_password(request: ForgotPasswordRequest, db: Session = Depends(get_db)):
    # التحقق من البريد أو رقم الهاتف
    user = None
    if request.email:
        user = db.query(User).filter(User.email == request.email).first()
    elif request.phone_number:
        user = db.query(User).filter(User.phone_number == request.phone_number).first()
    else:
        raise HTTPException(status_code=400, detail="يرجى إدخال البريد الإلكتروني أو رقم الهاتف")

    if not user:
        raise HTTPException(status_code=404, detail="المستخدم غير موجود")

    # إنشاء رمز إعادة تعيين
    reset_token = secrets.token_urlsafe(32)
    user.reset_token = reset_token
    user.token_expiration = datetime.utcnow() + timedelta(hours=1)
    db.commit()

    # طباعة الرابط (ممكن ترسليه لاحقًا عبر إيميل أو SMS)
    reset_link = f"http://localhost:8000/reset-password/{reset_token}"
    print("🔗 رابط إعادة تعيين كلمة المرور:", reset_link)

    return {"message": "تم إرسال رابط إعادة تعيين كلمة المرور"}