from fastapi import APIRouter, Depends, Form, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.place import Place
from schemas import PlaceOut
from datetime import datetime
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

router = APIRouter()

@router.post("/places")
def create_place(
    name: str = Form(...),
    description: str = Form(""),
    location: str = Form(""),
    price: float = Form(0.0),
    type: str = Form(None),
    db: Session = Depends(get_db)
):
    place = Place(
        name=name,
        description=description,
        location=location,
        price=price,
        type=type,
        created_at=datetime.utcnow()
    )
    

    db.add(place)
    db.commit()
    db.refresh(place)

    return place