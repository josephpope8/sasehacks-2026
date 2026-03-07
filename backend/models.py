from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CaretakerCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str

class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    timezone: str
    caretaker_id: Optional[str] = None

class MedicationCreate(BaseModel):
    patient_id: str
    name: str
    dosage: str
    time_to_take: str # Format: HH:MM:SS
    is_active: bool = True

class MedicationLogCreate(BaseModel):
    medication_id: str
    patient_id: str
    taken_at: Optional[datetime] = None
    status: str
    scheduled_for: datetime

class DailyCheckupCreate(BaseModel):
    patient_id: str
    mood: str
    notes: Optional[str] = None

class ReminderCreate(BaseModel):
    patient_id: str
    title: str
    description: Optional[str] = None
    time_to_remind: datetime
    is_active: bool = True
