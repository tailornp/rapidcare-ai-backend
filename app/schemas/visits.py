from pydantic import BaseModel

class VisitCreate(BaseModel):
    patient_id: int
    visit_date: str
    attending_physician: str
    notes: str
    symptoms: str
class VisitResponse(VisitCreate):
    id: int

    class Config:
        from_attributes = True