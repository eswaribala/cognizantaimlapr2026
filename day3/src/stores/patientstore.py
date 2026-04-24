
import sys
import os
from src.models.patient import Patient
from src.exceptions.patient_not_found_exception import PatientNotFoundException
# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)

from conf.logger_conf import setup_logger
logger = setup_logger("patientstore.log")
"""
create patient crud operation
"""
class PatientStore:
    def __init__(self):
        self.patients = []
    
    def add_patient(self, patient: Patient):
        logger.info(f"Adding patient: {patient}")
        self.patients.append(patient)

    def get_all_patients(self):
        return self.patients
    
    def get_patient_by_id(self, patient_id: int) -> Patient:
        logger.info(f"Searching Patient by id {patient_id}")
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        raise PatientNotFoundException(f"Patient with ID {patient_id} not found")
    
    def update_patient(self, patient_id: int, name: str = None, age: int = None):
        logger.info(f"Updating Patient by id {patient_id}")
        patient = self.get_patient_by_id(patient_id)
        if patient:
            if name:
                patient.name = name
            if age:
                patient.age = age
    
    def delete_patient(self, patient_id: int):
        logger.info(f"Deleting Patient by id {patient_id}")
        self.patients = [patient for patient in self.patients if patient.id != patient_id]