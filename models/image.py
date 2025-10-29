from tkinter import Image
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, nullable=False)  # ✅ يتطابق مع اسم العمود في قاعدة البيانات
    place_id = Column(Integer, ForeignKey("places.id")) # ربط الصورة بالمكان
    place = relationship("Place", back_populates="images") # علاقة مع نموذج المكان