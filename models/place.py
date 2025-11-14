from sqlalchemy import Column, Integer, String, Float, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    location = Column(String, nullable=True)
    price = Column(Float, nullable=False, default=0.0)
    type = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)

    # ✅ الحقول الجديدة
    number_of_rooms = Column(Integer, nullable=False, default=1)
    room_capacity = Column(Integer, nullable=False, default=1)

    # علاقات
    images = relationship("Image", back_populates="place", cascade="all, delete")
    reviews = relationship("Review", back_populates="place", cascade="all, delete")
    bookings = relationship("Booking", back_populates="place", cascade="all, delete")