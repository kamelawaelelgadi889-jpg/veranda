from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.contact import ContactMessage
from schemas import ContactInput

router = APIRouter()

@router.post("/contact")
def submit_contact_form(data: ContactInput, db: Session = Depends(get_db)):
    new_message = ContactMessage(**data.dict())
    db.add(new_message)
    db.commit()
    return {"message": "تم استلام رسالتك بنجاح، سنتواصل معك قريبًا"}