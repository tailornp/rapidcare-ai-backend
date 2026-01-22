from sqlalchemy.orm import Session
from app.models.visits import Visit
from datetime import datetime

def create_visit(
    db: Session,
    patient_id: int,
    visit_date: datetime,
    reason: str,
    symptoms: str = None,
    notes: str = None
):
    """
    Insert a new visit record into the visits table.
    
    Args:
        db: Database session
        patient_id: ID of the patient
        doctor_id: ID of the doctor
        visit_date: Date and time of the visit
        reason: Reason for the visit
        diagnosis: Diagnosis (optional)
        notes: Additional notes (optional)
    
    Returns:
        Visit: The created visit object
    """
    visit = Visit(
        patient_id=patient_id,
        visit_date=visit_date,
        reason=reason,
        symptoms=symptoms,
        notes=notes
    )
    
    db.add(visit)
    db.commit()
    db.refresh(visit)
    
    return visit