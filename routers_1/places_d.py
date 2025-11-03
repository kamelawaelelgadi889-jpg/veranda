from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.place import Place
from schemas import PlaceDelete

router = APIRouter()
#راوتر حدف المكان متتلخبطيش
@router.delete("/places_d/{place_id}")
def delete_place(place_id: int, db: Session = Depends(get_db)):
    place = db.query(Place).filter(Place.id == place_id).first()
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")

    db.delete(place)
    db.commit()
    return {"detail": f"Place '{place.name}' deleted successfully"}