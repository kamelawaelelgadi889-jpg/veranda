from fastapi import APIRouter, Depends, Form, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.place import Place
from schemas import PlaceOut
from datetime import datetime

router = APIRouter()

@router.post("/places", response_model=PlaceOut)
def create_place(
    name: str = Form(...),
    description: str = Form(""),
    location: str = Form(""),
    price: float = Form(0.0),
    type: str = Form(None),
    number_of_rooms: int = Form(...),
    room_capacity: int = Form(...),
    db: Session = Depends(get_db)
):
    place = Place(
        name=name,
        description=description,
        location=location,
        price=price,
        type=type,
        number_of_rooms=number_of_rooms,
        room_capacity=room_capacity,
        created_at=datetime.utcnow()
    )

    db.add(place)
    db.commit()
    db.refresh(place)

    return place