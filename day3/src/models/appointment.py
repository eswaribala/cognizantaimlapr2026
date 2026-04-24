"""
Create Appoinment 
"""
from datetime import date,time
from src.models.doctor import Doctor
from src.models.patient import Patient
class Appointment:
    """
    Appointment class
    """
    def __init__(self, id:int, date:date, time:time, doctor:Doctor, patient:Patient):
        self.appointment_id = id
        self.date = date
        self.time = time
        self.doctor = doctor
        self.patient = patient

    def __str__(self):
        return f"Appointment on {self.appointment_id} {self.date} at {self.time} with Dr. {self.doctor} for patient {self.patient}"