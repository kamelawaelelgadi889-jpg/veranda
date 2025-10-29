from sqlalchemy import Column, Integer, Float, ForeignKey, TIMESTAMP, String
from sqlalchemy.orm import relationship
from database import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    place_id = Column(Integer, ForeignKey("places.id"), nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String, nullable=False, default="pending")
    created_at = Column(TIMESTAMP, nullable=False)

    user = relationship("User", back_populates="bookings")
    place = relationship("Place", back_populates="bookings")