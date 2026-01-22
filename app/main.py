from fastapi import FastAPI
from app.database import engine
from app.models import patient, hospitalization, triage
from app.routers import patient as patient_router
from app.routers import triage as triage_router

patient.Base.metadata.create_all(bind=engine)
triage.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(patient_router.router)
app.include_router(triage_router.router)

@app.get("/health")
def health_check():
    return {"status": "active"}