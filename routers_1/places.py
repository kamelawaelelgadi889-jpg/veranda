from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.place import Place
from pydantic import BaseModel
from typing import List
from models.place import Place as PlaceSchema

router = APIRouter()

class PlaceInput(BaseModel):
    name: str
    description: str | None = None
    location: str | None = None

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/places")
def create_place(data: PlaceInput, db: Session = Depends(get_db)):
    new_place = Place(**data.dict())
    db.add(new_place)
    db.commit()
    db.refresh(new_place)
    return {
        "message": "✅ تم إضافة المكان",
        "place": {
            "id": new_place.id,
            "name": new_place.name,
            "location": new_place.location
        }
    }

@router.get("/places")
def get_places(db: Session = Depends(get_db)):
    places = db.query(Place).all()
    return places
print("راوتر الأماكن تم تحميله")
class PlaceSchema(BaseModel):
    id: int
    name: str
    description: str | None = None
    location: str | None = None

    class Config:
        orm_mode = True

@router.get("/places", response_model=List[PlaceSchema])
def get_all_places(db: Session = Depends(get_db)):
    return db.query(Place).all()