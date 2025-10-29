from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Booking
from models.place import Place
from datetime import datetime

router = APIRouter()

@router.post("/bookings")
def create_booking(
    user_id: int = Form(...),
    place_id: int = Form(...),
    db: Session = Depends(get_db)
):
    # نجيب المكان من قاعدة البيانات
    place = db.query(Place).filter(Place.id == place_id).first()
    if not place:
        raise HTTPException(status_code=404, detail="المكان غير موجود")

    # نستخدم السعر من المكان
    booking = Booking(
        user_id=user_id,
        place_id=place_id,
        price=place.price,
        status="pending",
        created_at=datetime.utcnow()
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return {
        "message": "تم إنشاء الحجز",
        "booking": {
            "id": booking.id,
            "user_id": booking.user_id,
            "place_id": booking.place_id,
            "price": booking.price,
            "status": booking.status,
            "created_at": str(booking.created_at)
        }
    }