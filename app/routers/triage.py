from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.triage import TriageCreate, TriageResponse
from app.services.triage import create_triage_entry, get_triages_by_date, assess_severity

router = APIRouter(prefix="/triage", tags=["triage"])

@router.post("/", response_model=TriageResponse)
def create_patient(triage: TriageCreate, db: Session = Depends(get_db)):
   entry = create_triage_entry(triage, db)
   assess_severity(triage.symptoms, triage.notes, str(triage.patient_id), db, entry.id)
   return entry

@router.get("/{triage_date}", response_model=list[TriageResponse])
def get_patient(triage_date: str, db: Session = Depends(get_db)):
    return get_triages_by_date(triage_date, db)
 
# @router.get("/llm_test/")
# def llm_test(symptoms: str = "Severe chest pain and shortness of breath", patient_id: str = "1", db: Session = Depends(get_db)):
#     symptoms = "Severe chest pain and shortness of breath"
#     patient_id = "1"
#     response = assess_severity(symptoms, patient_id, db)
#     return {"response": response}