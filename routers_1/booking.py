from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.booking import Booking
from models.place import Place
from schemas import BookingCreate, BookingOut
from datetime import datetime

router = APIRouter()

@router.post("/bookings", response_model=BookingOut)
def create_booking(data: BookingCreate, db: Session = Depends(get_db)):
    place = db.query(Place).filter(Place.id == data.place_id).first()
    if not place:
        raise HTTPException(status_code=404, detail="المكان غير موجود")

    booking = Booking(
        user_id=data.user_id,
        place_id=data.place_id,
        price=place.price,
        status="pending",
        guests=data.guests,
        check_in=data.check_in,
        check_out=data.check_out,
        created_at=datetime.utcnow()
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking