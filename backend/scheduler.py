from apscheduler.schedulers.background import BackgroundScheduler
from database import supabase
from datetime import datetime
import pytz

def trigger_telecom_script(patient, medication):
    # This is a placeholder for the telecom engineer's script
    print(f"\n[TELECOM SCRIPT TRIGGERED]")
    print(f"Time to call: {patient['first_name']} {patient['last_name']} at {patient['phone_number']}")
    print(f"Message: Time to take your {medication['dosage']} of {medication['name']}")
    print("-" * 30)

def check_medications():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Checking medications list...")
    
    # In a production system, you'd evaluate timezones, but for simplicity,
    # we'll assume the server time and db schedule times align for now.
    current_time_str = datetime.now().strftime('%H:%M:00')

    try:
        # Fetch active medications that match the current time (ignoring seconds)
        # Note: If time format in DB is like '08:00:00', this exact match works.
        meds_response = supabase.table("medications").select("*, patients(*)").eq("is_active", True).execute()
        
        if meds_response.data:
            for med in meds_response.data:
                # Check if it's the right time down to the minute
                # Suppose time_to_take is stored as '08:00:00'
                if med['time_to_take'].startswith(current_time_str[:5]):
                    trigger_telecom_script(med['patients'], med)

    except Exception as e:
        print(f"Error checking medications: {e}")

# Initialize scheduler
scheduler = BackgroundScheduler()
# Run every minute
scheduler.add_job(check_medications, 'cron', minute='*')
