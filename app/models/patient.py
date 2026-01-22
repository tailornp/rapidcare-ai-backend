from sqlalchemy import Column, Integer, String, TEXT, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    patient_code = Column(String, unique=True, index=True, nullable=True)
    date_of_birth = Column(String)
    sex_at_birth = Column(String)
    email = Column(String)
    mobile_number = Column(String)
    address = Column(String)
    emergency_contact = Column(String)
    insurance_details = Column(TEXT)
    chronic_conditions = Column(TEXT)
    allergies = Column(TEXT)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


