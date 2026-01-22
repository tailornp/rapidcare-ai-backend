from pydantic import BaseModel

class HospitalizationCreate(BaseModel):
    patient_id: int
    admission_date: str
    discharge_date: str
    reason_for_admission: str
    attending_physician: str
    room_number: str
    notes: str

class HospitalizationResponse(HospitalizationCreate):
    id: int

    class Config:
        from_attributes = True