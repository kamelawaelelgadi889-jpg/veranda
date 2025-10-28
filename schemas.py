from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date
from decimal import Decimal



# نموذج الإدخال لنموذج الاتصال
class ConactInput(BaseModel): 
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
    total_price: Decimal

# نموذج طلب إعادة تعيين كلمة المرور
class EmailRequest(BaseModel):
    email: str
    #هادلا لو نبي ندير تغيير كلمة المرور حتي ب رقم هاتف لاكن لازم يبي حاجات تانية ف ممكن نديرها في الاخير 
    #email : Optional[str] = None
    # phone_number : Optional[str] = None

# نموذج الإدخال لتسجيل الدخول
class loginInput(BaseModel):
    email: EmailStr
    password: str

# نموذج الإدخال لإضافة مكان
class PlaceInput(BaseModel):
    name: str
    description: str | None = None
    location: str | None = None

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
