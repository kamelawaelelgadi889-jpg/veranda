from sqlalchemy import Column, Integer, String, ForeignKey, Date, DECIMAL, PrimaryKeyConstraint
from database import Base
from sqlalchemy.orm import relationship
class Booking(Base):
    __tablename__="bookings"
    id=Column(Integer, primary_key=True, index=True )
    user_id = Column(Integer, ForeignKey("users.id"))
    place_id = Column(Integer, ForeignKey("places.id"))
    check_in =Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)
    guests = Column(Integer, nullable=False)
    total_price = Column(DECIMAL(10, 2), nullable=False)
    status = Column(String, default="pending")
    user = relationship("User", back_populates="bookings")
    place = relationship("Place", back_populates="bookings")
    def __repr__(self):
        return f"<Booking(id={self.id}, user_id={self.user_id}, place_id={self.place_id}, check_in={self.check_in}, check_out={self.check_out}, guests={self.guests}, total_price={self.total_price}, status={self.status}>"
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id ,
            "place_id": self.place_id,
            "check_in":self.check_in,
            "check_out": self.check_out,
            "guests": self.guests,
            "total_price": self.total_price,
            "status": self.status
               }
    


