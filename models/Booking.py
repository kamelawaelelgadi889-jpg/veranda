from sqlalchemy import Column, DateTime, Integer, Float, String, ForeignKey, TIMESTAMP, Date
from sqlalchemy.orm import relationship
from database import Base
from models.user import User
from models.place import Place

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    place_id = Column(Integer, ForeignKey("places.id"))

    username = Column(String)
    email = Column(String)
    phone_number = Column(String)
    notes = Column(String)
    price = Column(Float)
    status = Column(String)
    check_in = Column(DateTime)
    check_out = Column(DateTime)
    created_at = Column(DateTime)

    user = relationship("User", back_populates="bookings")
    place = relationship("Place", back_populates="bookings")
