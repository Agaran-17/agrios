from pydantic import BaseModel
from typing import Optional


class FarmerCreate(BaseModel):
    name: str
    phone_number: str
    password: str
    district: str
    land_size: Optional[float] = None
    preferred_language: Optional[str] = "ta"


class FarmerOut(BaseModel):
    id: int
    name: str
    phone_number: str
    district: str
    land_size: Optional[float] = None
    preferred_language: str

    class Config:
        from_attributes = True