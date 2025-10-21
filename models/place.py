from sqlalchemy import Column, Integer, String, Text
from database import Base
from sqlalchemy.orm import relationship

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    location = Column(String(100), nullable=True)

    bookings = relationship("Booking", back_populates="place")

 