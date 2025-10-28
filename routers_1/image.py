from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.image import Image
from schemas import ImageInput

router = APIRouter()
@router.post("/images")
def add_image(image: ImageInput, db: Session = Depends(get_db)):
    new_image = Image(**image.dict())
    db.add(new_image)
    db.commit()
    db.refresh(new_image)
    return new_image

@router.get("/places/{place_id}/images")
def get_place_images(place_id: int, db: Session = Depends(get_db)):
    return db.query(Image).filter(Image.place_id == place_id).all()

print("راوتر الصور تم تحميله")