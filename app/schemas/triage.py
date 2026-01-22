from pydantic import BaseModel

class TriageCreate(BaseModel):
    patient_id: int
    symptoms: str
    notes: str
    triage_date: str

class TriageResponse(BaseModel):
    id: int
    patient_id: int
    visit_id: int
    status: str
    severity_score: str | None

    class Config:
        from_attributes = True