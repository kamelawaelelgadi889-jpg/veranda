from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date , datetime
from decimal import Decimal



# نموذج الإدخال لنموذج الاتصال
class ContactInput(BaseModel): 
    full_name: str 
    email: EmailStr
    phone_number: str
    message: str
    user_id: Optional[int] = None

#  نموذج الإدخال للحجز
class BookingInput(BaseModel):
    user_id: int
    place_id: int
    check_in: date
    check_out: date
    guests: int
# نموذج الإخراج للحجز

class BookingOut(BaseModel):
    id: int
    user_id: int
    place_id: int
    price: float
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
# نموذج طلب إعادة تعيين كلمة المرور
class EmailRequest(BaseModel):
    email: EmailStr
    #هادلا لو نبي ندير تغيير كلمة المرور حتي ب رقم هاتف لاكن لازم يبي حاجات تانية ف ممكن نديرها في الاخير 
    #email : Optional[str] = None
    # phone_number : Optional[str] = None

# نموذج الإدخال لتسجيل الدخول
class loginInput(BaseModel):
    email: EmailStr
    password: str

# نموذج الإدخال لإضافة مكان
class PlaceCreate(BaseModel):
    name: str
    description: Optional[str] = ""
    location: Optional[str] = ""
    price: float = 0.0
    type: Optional[str] = None

class PlaceOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    location: Optional[str]
    price: float
    type: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

# نموذج الإدخال لتسجيل المستخدم
class UserInput(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    phone_number: str

# نموذج طلب إعادة تعيين كلمة المرور
class ResetRequest(BaseModel):
    new_password: str

class ImageInput(BaseModel):
    place_id: int
    image_url: str

#ادخال التقيمات 
class ReviewCreate(BaseModel):
    user_id: int
    place_id: int
    rating: int
    comment: Optional[str] = ""


#
    class ReviewOut(BaseModel):
        id: int
        user_id: int
        place_id: int
        rating: int
        comment: Optional[str] 
        created_at: datetime
        class Config:
            orm_mode = True


