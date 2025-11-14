from fastapi import APIRouter, Depends
from security import get_current_user

router = APIRouter()

@router.get("/dashboard")
def get_dashboard(user_id: str = Depends(get_current_user)):
    return {"message": f"تم تسجيل الدخول كمسؤول "}
    