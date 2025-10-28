from fastapi import FastAPI
from routers_1 import register,login,image
from routers_1 import booking ,places,calendar,forgot_password,reset_password,contact
from sqlalchemy import text
from database import SessionLocal




app = FastAPI()

app.include_router(register.router)
app.include_router(login.router)
app.include_router(booking.router)
app.include_router(places.router)
app.include_router(calendar.router)
app.include_router(forgot_password.router)
app.include_router(reset_password.router)
app.include_router(contact.router)
app.include_router(image.router)
 
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


