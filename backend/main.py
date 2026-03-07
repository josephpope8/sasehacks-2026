from fastapi import FastAPI, HTTPException
from database import supabase
from models import PatientCreate, MedicationCreate

app = FastAPI(title="Elder Reminder API")

@app.post("/add-patient")
def add_patient(patient: PatientCreate):
    try:
        data = supabase.table("patients").insert(patient.model_dump(exclude_unset=True)).execute()
        return {"message": "Patient added successfully", "data": data.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/add-medication")
def add_medication(medication: MedicationCreate):
    try:
        data = supabase.table("medications").insert(medication.model_dump(exclude_unset=True)).execute()
        return {"message": "Medication added successfully", "data": data.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Start the background task scheduler when FastAPI launches
from scheduler import scheduler
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting background scheduler...")
    scheduler.start()
    yield
    print("Shutting down scheduler...")
    scheduler.shutdown()

app.router.lifespan_context = lifespan
