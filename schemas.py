from pydantic import BaseModel, EmailStr
from types import Optional

class ConactInput(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: str
    message: str
    user_id: Optional[int] = None