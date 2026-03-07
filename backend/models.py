from pydantic import BaseModel
from typing import Optional

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
