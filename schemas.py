from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import date , datetime
from decimal import Decimal



# نموذج الإدخال لنموذج الاتصال
class ContactInput(BaseModel): 
    full_name: str 
    email: EmailStr
   # phone_number: str
    message: str
  #  user_id: Optional[int] = None

#  نموذج الإدخال للحجز
class BookingCreate(BaseModel):
    full_name: str
    email: str
    phone_number: str
    notes: str | None = None
    check_in: datetime
    check_out: datetime

# نموذج الإخراج للحجز

class BookingOut(BaseModel):
    id: int
    user_id: int
    place_id: int
    price: float
    status: str
    #guests: int
    check_in: date
    check_out: date
    created_at: datetime

    class Config:
        orm_mode = True

# نموذج طلب إعادة تعيين كلمة المرور
class EmailRequest(BaseModel):
    email: EmailStr

# نموذج الإدخال لتسجيل الدخول
class loginInput(BaseModel):
    email: EmailStr
    password: str

# نموذج الإدخال لإضافة مكان
class PlaceCreate(BaseModel):
    name: str
    description: Optional[str]
    location: Optional[str]
    price: float
    type: Optional[str]
    number_of_rooms: int
    room_capacity: int


class PlaceOut(BaseModel):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True




#حدف الاماكن
class PlaceDelete(BaseModel):
    id: int

# نموذج الإدخال لتسجيل المستخدم
class UserInput(BaseModel):
    username: str
    email: EmailStr
    password: str
    #phone_number: str
    #role: Optional[str] = "user"

    
# نموذج طلب إعادة تعيين كلمة المرور (إعادة التعيين باستخدام توكن أو رابط)
class ForgotPasswordRequest(BaseModel):
    email: Optional[str] = None
    phone_number: Optional[str] = None

class ResetPasswordRequest(BaseModel):
    new_password: str

# ادخال التقيمات 

class ReviewCreate(BaseModel):
    user_id: int
    place_id: int
    rating: int
    comment: Optional[str] = ""

class ReviewOut(BaseModel):
    id: int
    user_id: int
    place_id: int
    rating: int
    comment: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True


#لحالة الحجز
#حاله الحجز في الداش بورد مش نعدل عليها بروحي 
class booking_status_update(BaseModel):
    status: str


class imageCreate(BaseModel):
    place_id: int
    image_url: str
