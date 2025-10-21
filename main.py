from fastapi import FastAPI
from routers_1 import register,login
from routers_1 import booking ,places,calendar
from sqlalchemy import text
from database import SessionLocal



app = FastAPI()
app.include_router(register.router)
app.include_router(login.router)
app.include_router(booking.router)
app.include_router(places.router)
app.include_router(calendar.router)
 
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


