"""
create appoinment store
"""
import sys
import os
from src.models.appointment import Appointment
from src.exceptions.appointment_not_found_exception import AppointmentNotFoundException
# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)

from conf.logger_conf import setup_logger
logger = setup_logger("appointmentstore.log")
class AppointmentStore:
    def __init__(self):
        self.appointments = []
    def add_appointment(self, appointment: Appointment):
        logger.info(f"Adding appointment: {appointment}")
        self.appointments.append(appointment)
    def get_all_appointments(self):
        logger.info("Fetching all appointments")
        return self.appointments
    def get_appointment_by_id(self, appointment_id: int) -> Appointment:
        logger.info(f"Fetching appointment with ID: {appointment_id}")
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                return appointment
        raise AppointmentNotFoundException(f"Appointment with ID {appointment_id} not found")
    def update_appointment(self, appointment_id: int, doctor_id: int = None, patient_name: str = None, date: str = None):
        appointment = self.get_appointment_by_id(appointment_id)
        logger.info(f"Updating appointment with ID: {appointment_id}")
        if appointment:
            if doctor_id:
                appointment.doctor_id = doctor_id
            if patient_name:
                appointment.patient_name = patient_name
            if date:
                appointment.date = date
    def delete_appointment(self, appointment_id: int):
        logger.info(f"Deleting appointment with ID: {appointment_id}")
        self.appointments = [appointment for appointment in self.appointments if appointment.appointment_id != appointment_id]

