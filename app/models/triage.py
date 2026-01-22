from sqlalchemy import Column, ForeignKey, Integer, String, func, DateTime
from app.database import Base

class Triage(Base):
    __tablename__ = "triages"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, index=True)
    triage_date = Column(DateTime)
    visit_id = Column(Integer, ForeignKey("visits.id"), index=True)
    severity_score = Column(String, nullable=True)
    status = Column(String)
    sequence_number = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())