from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.user import User  # SQLAlchemy model
from pydantic import BaseModel, EmailStr
import hashlib

router = APIRouter()

# Pydantic schema for input
class UserInput(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    phone_number: str

# DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserInput, db: Session = Depends(get_db)):
    # تحقق من طول كلمة السر
    if len(user.password) < 8:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=" يجب ان تتكون كلمة السر من 8 حروف او ارقام على الاقل"
        )

    # تحقق من وجود الإيميل مسبقاً
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="البريد الالكتروني مستخدما مسبقا"
        )

    # تشفير كلمة السر
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()

    # إنشاء مستخدم جديد
    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password_hash=hashed_password,
        phone_number=user.phone_number
    )

    # حفظ في قاعدة البيانات
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "تم تسجيل المستخدم بنجاح 🎉",
        "user": {
            "id": new_user.id,
            "full_name": new_user.full_name,
            "email": new_user.email,
            "phone_number": new_user.phone_number
        }
    }