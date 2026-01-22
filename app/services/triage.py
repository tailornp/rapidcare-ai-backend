from app.models.triage import Triage
from app.models.visits import Visit
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.services.ollama import get_llm_response
from app.services.patients import get_patient_service
from app.utils.get_age import get_age
def create_triage_entry(triage, db: Session):
    print(triage)
    try:
        # Create a new visit
        visit = Visit(
            patient_id=triage.patient_id,
            visit_date=triage.triage_date,
            symptoms=triage.symptoms,
            notes=triage.notes
        )
        db.add(visit)
        db.flush()  # Get visit ID without committing
        
        # Get the last sequence number and increment
        last_sequence = db.query(func.max(Triage.sequence_number)).scalar()
        new_sequence = (last_sequence or 0) + 1
        
        # Create triage entry
        triage_entry = Triage(
            patient_id=triage.patient_id,
            visit_id=visit.id,
            triage_date=triage.triage_date,
            status="active",
            sequence_number=new_sequence,
        )
        db.add(triage_entry)
        db.commit()
        
        return triage_entry
        
    except Exception as e:
        db.rollback()
        raise e
    



def get_triages_by_date(triage_date: str, db: Session) -> list[Triage]:
    date = datetime.strptime(triage_date, "%Y-%m-%d")
    start_of_day = date.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = date.replace(hour=23, minute=59, second=59, microsecond=999999)
        
    triages = db.query(Triage).filter(
        Triage.triage_date >= start_of_day,
        Triage.triage_date <= end_of_day
    ).order_by(Triage.severity_score.desc()).all()
        
    return triages

def assess_severity(symptoms: str, notes: str, patient_id: str, db: Session, triage_id) -> str:
    patient = get_patient_service(int(patient_id), db=db)
   
    # Convert string date (YYYY-MM-DD) to date object
    dob = datetime.strptime(patient.date_of_birth, "%Y-%m-%d").date()
    age = get_age(dob)
    
    prompt = f"""You are a clinical triage assistant. Based only on the following patient details, provide a score accurately between 1 to 10 upto 2 decimal places. Where 1 means very low urgency and 10 mean life threatening. 
Important: Only output number.

Patient information
Age: {age}
Sex: {patient.sex_at_birth}
Symptoms: {symptoms}
Allergies: {patient.allergies}
Notes: {notes}
Chronic conditions: {patient.chronic_conditions}"""
    response = get_llm_response(prompt)
    
    # Extract severity score from response
    severity_score = response.strip()
    
    # Update triage entry with severity score
    triage = db.query(Triage).filter(Triage.id == triage_id).first()
    if triage:
        triage.severity_score = severity_score
        db.commit()
    
    return severity_score