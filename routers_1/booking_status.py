from fastapi import APIRouter, Form, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.booking import Booking
#نغير في حاله  الs tsatus
router = APIRouter()
@router.put("/booking/{booking_id}/status")
def update_booking_status(
    booking_id: int,
    new_status: str=Form(...),
    db: Session = Depends(get_db)
):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    booking.status = new_status
    db.commit()
    db.refresh(booking)

    return {"detail": f"Booking status updated to '{new_status}'"}