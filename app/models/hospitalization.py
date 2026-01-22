from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Hospitalization(Base):
    __tablename__ = "hospitalizations"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), index=True)
    admission_date = Column(String)
    discharge_date = Column(String)
    reason_for_admission = Column(String)
    attending_physician = Column(String)
    room_number = Column(String)
    notes = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())