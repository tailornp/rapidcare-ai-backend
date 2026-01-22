from sqlalchemy import TEXT, Column, ForeignKey, Integer, String
from app.database import Base   
    
class Visit(Base):
    __tablename__ = "visits"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), index=True)
    visit_date = Column(String)
    symptoms = Column(TEXT)
    attending_physician = Column(String, nullable=True )
    notes = Column(String)