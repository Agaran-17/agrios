from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.schemas.farmer import FarmerCreate, FarmerOut
from app.auth import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/farmers", tags=["farmers"])


@router.post("/register", response_model=FarmerOut)
def register_farmer(farmer: FarmerCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Farmer).filter(
        models.Farmer.phone_number == farmer.phone_number
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Phone number already registered")

    new_farmer = models.Farmer(
        name=farmer.name,
        phone_number=farmer.phone_number,
        hashed_password=hash_password(farmer.password),
        district=farmer.district,
        land_size=farmer.land_size,
        preferred_language=farmer.preferred_language,
    )
    db.add(new_farmer)
    db.commit()
    db.refresh(new_farmer)
    return new_farmer


@router.post("/login")
def login_farmer(phone_number: str, password: str, db: Session = Depends(get_db)):
    farmer = db.query(models.Farmer).filter(
        models.Farmer.phone_number == phone_number
    ).first()
    if not farmer or not verify_password(password, farmer.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid phone number or password")

    token = create_access_token({"sub": str(farmer.id)})
    return {"access_token": token, "token_type": "bearer"}