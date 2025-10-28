from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from models.user import User
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime, timedelta
from typing import Optional
import secrets
from schemas import EmailRequest

from routers_1.reset_password import ResetRequest

router = APIRouter()



@router.post("/forgot-password")
def forgot_password(request: ResetRequest, db: Session = Depends(get_db)):
    if request.email:
        user = db.query(User).filter(User.email == request.email).first()
    elif request.phone_number:
        user = db.query(User).filter(User.phone_number == request.phone_number).first()
    else:
        raise HTTPException(status_code=400, detail="يرجى إدخال البريد الإلكتروني أو رقم الهاتف")

    if not user:
        raise HTTPException(status_code=404, detail="المستخدم غير موجود")

    reset_token = secrets.token_urlsafe(32)
    user.reset_token = reset_token
    user.token_expiration = datetime.utcnow() + timedelta(hours=1)
    db.commit()

    reset_link = f"http://localhost:8000/reset-password/{reset_token}"
    print("🔗 رابط إعادة تعيين كلمة المرور:", reset_link)

    return {"message": "تم إرسال رابط إعادة تعيين كلمة المرور"}
