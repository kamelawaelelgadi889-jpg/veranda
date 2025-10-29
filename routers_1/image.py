from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.image import Image
import os
import shutil

router = APIRouter()
UPLOAD_DIR = "static/images"

@router.post("/images")
def add_image(
    place_id: int = Form(...),
    image_url: str = Form(None),
    file: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    print("📥 البيانات المستلمة:")
    print("place_id:", place_id)
    print("image_url:", image_url)
    print("file:", file.filename if file is not None else "لا يوجد ملف")

    if file is not None and getattr(file, "filename", None):
        os.makedirs(UPLOAD_DIR, exist_ok=True)
        filename = os.path.basename(file.filename)
        file_path = os.path.join(UPLOAD_DIR, filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        try:
            file.file.close()
        except Exception:
            pass
        image_url = f"/{UPLOAD_DIR.replace(os.sep, '/')}/{filename}"
        image = Image(place_id=place_id, image_url=image_url)

    elif image_url:
        image = Image(place_id=place_id, image_url=image_url)

    else:
        raise HTTPException(status_code=400, detail="يجب إرسال صورة أو رابط")

    db.add(image)
    db.commit()
    db.refresh(image)

    return {
        "message": "تم حفظ الصورة",
        "image": {
            "id": getattr(image, "id", None),
            "place_id": image.place_id,
            "image_url": image.image_url
        }
    }