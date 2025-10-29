from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from pydantic import EmailStr as EmailStr
from database import SessionLocal
from sqlalchemy.orm import Session
from models.user import User
import hashlib
from fastapi import Depends
from schemas import loginInput
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(credentials: loginInput, db: Session = Depends(get_db)):
    # تشفير كلمة السر المدخلة
    hashed_password = hashlib.sha256(credentials.password.encode()).hexdigest()

    # البحث عن المستخدم
    user = db.query(User).filter(
        User.email == credentials.email,
        User.password_hash == hashed_password
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="الإيميل أو كلمة السر غير صحيحة"
        )

    return {
        "message": "تم تسجيل الدخول بنجاح ✅",
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "phone_number": user.phone_number
        }
    }
