from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.patient import PatientCreate, PatientResponse
from app.models.patient import Patient
from app.utils.base62 import encode_base62

PREFIX = "P"


def create_patient_service(patient: PatientCreate, db: Session) -> PatientResponse:
    
    db_patient = Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    encoded = encode_base62(db_patient.id)
    db_patient.patient_code = f"{PREFIX}-{encoded}"
    db.commit()
    db.refresh(db_patient)
    return db_patient


def get_patient_service(patient_id: int, db: Session) -> PatientResponse:
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient