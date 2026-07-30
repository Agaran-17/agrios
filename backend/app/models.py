from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Farmer(Base):
    __tablename__ = "farmers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    district = Column(String, nullable=False)
    land_size = Column(Float, nullable=True)
    preferred_language = Column(String, default="ta")