from pydantic import BaseModel, Field

class PatientCreate(BaseModel):
    name: str = Field(..., title="First Name", max_length=50)
    date_of_birth: str = Field(..., title="Date of Birth", pattern=r'^\d{4}-\d{2}-\d{2}$')  # YYYY-MM-DD format
    patient_code: str | None = Field(None, title="Patient Code", max_length=20)
    sex_at_birth: str = Field(..., title="Sex at Birth", max_length=10)
    email: str = Field(..., title="Email Address", max_length=100)
    mobile_number: str = Field(..., title="Mobile Number", max_length=15)
    address: str = Field(..., title="Residential Address", max_length=200)
    emergency_contact: str = Field(..., title="Emergency Contact", max_length=100)
    insurance_details: str = Field(..., title="Insurance Details")  
    chronic_conditions: str = Field(..., title="Chronic Conditions")
    allergies: str = Field(..., title="Allergies")

class PatientResponse(PatientCreate):
    id: int

    class Config:
        from_attributes = True