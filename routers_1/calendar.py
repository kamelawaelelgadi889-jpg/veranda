from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.booking import Booking

router = APIRouter()

@router.get("/calendar/{place_id}/booked-dates")
def get_booked_dates(place_id: int, db: Session = Depends(get_db)):
    bookings = db.query(Booking).filter(
        Booking.place_id == place_id,
        Booking.status.in_(["pending", "confirmed"])
    ).all()

    booked_periods = []
    for booking in bookings:
        booked_periods.append({
            "check_in": booking.check_in.strftime("%Y-%m-%d"),
            "check_out": booking.check_out.strftime("%Y-%m-%d")
        })

    return {
        "place_id": place_id,
        "booked_periods": booked_periods
    }