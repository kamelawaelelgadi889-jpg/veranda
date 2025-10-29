from fastapi import APIRouter, HTTPException, status, Depends, Form
from sqlalchemy.orm import Session
from database import get_db
from models.review import Review
from datetime import datetime

router = APIRouter()

@router.post("/review")
def add_review(
    user_id: int= Form(...),
    place_id: int= Form(...),
    rating: int = Form(...),
    comment: str = Form(""),
    db: Session = Depends(get_db)
):
    print("ريفيو جديد:")
    print("user_id:",user_id)
    print("place_id:",place_id)
    print("rating:",rating)
    print("comment:",comment)

    if rating < 1 or rating > 5:
        raise HTTPException(status_code=400, detail="التقييم يجب أن يكون بين 1 و 5")
    review = Review(
       user_id=user_id,
       place_id=place_id,
       rating=rating,
       comment=comment,
       created_at=datetime.utcnow()
    )
    db.add(review)
    db.commit()
    db.refresh(review)
    return review

    