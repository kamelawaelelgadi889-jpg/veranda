from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.Booking import Booking
from datetime import timedelta

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/calendar/{place_id}/booked-dates")
def get_booked_dates(place_id: int, db: Session = Depends(get_db)):
    bookings = db.query(Booking).filter(Booking.place_id == place_id).all()
    if not bookings:
        return {"message": "لا توجد حجوزات لهذا المكان.", "booked_dates": []}

    booked_dates = []
    for booking in bookings:
        current_date = booking.check_in
        while current_date <= booking.check_out:
            booked_dates.append(current_date.strftime("%Y-%m-%d"))  # صيغة واضحة
            current_date += timedelta(days=1)

    return {
        "place_id": place_id,
        "booked_dates": booked_dates
    }

print("✅ راوتر التقويم تم تحميله")