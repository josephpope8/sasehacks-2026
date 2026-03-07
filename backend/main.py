from fastapi import FastAPI, HTTPException
from database import supabase
from models import (
    CaretakerCreate, PatientCreate, MedicationCreate,
    MedicationLogCreate, DailyCheckupCreate, ReminderCreate
)
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

@app.post("/add-caretaker")
def add_caretaker(caretaker: CaretakerCreate):
    try:
        data = supabase.table("caretakers").insert(caretaker.model_dump(exclude_unset=True)).execute()
        return {"message": "Caretaker added successfully", "data": data.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/add-medication-log")
def add_medication_log(log: MedicationLogCreate):
    try:
        data = supabase.table("medication_logs").insert(log.model_dump(exclude_unset=True, mode='json')).execute()
        return {"message": "Medication log added successfully", "data": data.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/add-daily-checkup")
def add_daily_checkup(checkup: DailyCheckupCreate):
    try:
        data = supabase.table("daily_checkups").insert(checkup.model_dump(exclude_unset=True)).execute()
        return {"message": "Daily checkup added successfully", "data": data.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/add-reminder")
def add_reminder(reminder: ReminderCreate):
    try:
        data = supabase.table("reminders").insert(reminder.model_dump(exclude_unset=True, mode='json')).execute()
        return {"message": "Reminder added successfully", "data": data.data}
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
