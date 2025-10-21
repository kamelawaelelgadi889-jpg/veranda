from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from database import SessionLocal
from models.Booking import Booking
from decimal import Decimal
from datetime import date

router = APIRouter()

# نموذج الإدخال بدون status
class BookingInput(BaseModel):
    user_id: int
    place_id: int
    check_in: date
    check_out: date
    guests: int
    total_price: Decimal

# دالة الاتصال بقاعدة البيانات
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# راوتر الحجز
@router.post("/booking")
def booking(booking: BookingInput, db: Session = Depends(get_db)):
    new_booking = Booking(
        user_id=booking.user_id,
        place_id=booking.place_id,
        check_in=booking.check_in,
        check_out=booking.check_out,
        guests=booking.guests,
        total_price=booking.total_price,
        status="pending"  # ← الحالة تبدأ تلقائيًا بـ pending
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return {
        "message": "تم إرسال الحجز، في انتظار موافقة الإدارة ✅",
        "booking": {
            "id": new_booking.id,
            "user_id": new_booking.user_id,
            "place_id": new_booking.place_id,
            "check_in": new_booking.check_in,
            "check_out": new_booking.check_out,
            "guests": new_booking.guests,
            "total_price": new_booking.total_price,
            "status": new_booking.status
        }
    }


print("✅ راوتر الحجز تم تحميله بنجاح")

