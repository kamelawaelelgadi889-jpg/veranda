from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from database import get_db
from models.booking import Booking
from models.place import Place
from models.user import User
from schemas import BookingCreate, BookingOut
from datetime import datetime

router = APIRouter()

@router.post("/places/{place_id}/bookings", response_model=BookingOut)
def create_booking_for_place(
    place_id: int,
    data: BookingCreate,
    db: Session = Depends(get_db)
):
    # تحقق من وجود المكان
    place = db.query(Place).filter(Place.id == place_id).first()
    if not place:
        raise HTTPException(status_code=404, detail="المكان غير موجود")

    # تحقق من التداخل
    overlapping = db.query(Booking).filter(
        Booking.place_id == place_id,
        Booking.check_out >= data.check_in,
        Booking.check_in <= data.check_out
    ).first()

    if overlapping:
        raise HTTPException(status_code=400, detail="المكان محجوز في هذه الفترة")

    # تحقق أو إنشاء المستخدم
    user = db.query(User).filter(
        User.email == data.email,
        User.phone_number == data.phone_number
    ).first()

    if not user:
        user = User(
            username=data.full_name,
            email=data.email,
            phone_number=data.phone_number,
            created_at=datetime.utcnow()
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    # إنشاء الحجز
    booking = Booking(
        user_id=user.id,
        place_id=place.id,
        username=data.full_name,
        email=data.email,
        phone_number=data.phone_number,
        notes=data.notes,
        price=place.price,
        status="pending",
        check_in=data.check_in,
        check_out=data.check_out,
        created_at=datetime.utcnow()
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking