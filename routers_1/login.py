from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.user import User
from schemas import loginInput
import hashlib
from jose import jwt
from datetime import datetime, timedelta

# إعدادات التوكن
SECRET_KEY = "your-secret-key"  # غيّره في بيئة الإنتاج
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ADMIN_ROLE = "admin"

router = APIRouter()

# دالة توليد التوكن
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# الاتصال بقاعدة البيانات
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# راوتر تسجيل الدخول
@router.post("/login")
def login(credentials: loginInput, db: Session = Depends(get_db)):
    # تشفير كلمة المرور
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

    # التحقق من الدور
    if user.role == ADMIN_ROLE:
        # توليد التوكن للمسؤول
        access_token = create_access_token(
            data={"sub": str(user.id)},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return {
            "message": "تم تسجيل الدخول كمشرف ✅",
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "phone_number": user.phone_number,
                "role": user.role
            }
        }
    else:
        # تسجيل دخول عادي بدون توكن
        return {
            "message": "تم تسجيل الدخول كمستخدم عادي ✅",
            "access_token": None,
            "token_type": None,
            "user": {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "phone_number": user.phone_number,
                "role": user.role
            }
        }