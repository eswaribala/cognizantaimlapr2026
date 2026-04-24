"""
test for doctor contract
"""
import sys
import os
import pytest
import csv

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)
from src.models.doctor import Doctor
"""
test for doctor object created
"""
@pytest.fixture
def initialize_doctor():
    """
    initialize doctor object
    """
    doctor = Doctor(id=1, name="Dr. Smith", specialization="Cardiology")
    return doctor

def read_doctor_data_from_csv():
    """
    read doctor data from csv file
    """
    doctor_data = []
    with open('tests/doctors.csv', mode='r', newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            doctor_data.append((int(row['id']), row['name'], row['specialization']))
    return doctor_data


def test_doctor_creation(initialize_doctor):
    """
    test doctor object created
    """
    doctor = initialize_doctor
    assert doctor.id == 1
    assert doctor.name == "Dr. Smith"
    assert doctor.specialization == "Cardiology"

@pytest.mark.parametrize("id, name, specialization", [
    (1, "Dr. Smith", "Cardiology"),
    (2, "Dr. Johnson", "Neurology"),
    (3, "Dr. Lee", "Pediatrics"),
])
def test_parameterized_doctor_creation(id, name, specialization):
    doctor = Doctor(id=id, name=name, specialization=specialization)
    assert doctor.id == id
    assert doctor.name == name
    assert doctor.specialization == specialization

@pytest.mark.parametrize("id, name, specialization", read_doctor_data_from_csv())
def test_parameterized_csv_doctor_creation(id, name, specialization):
    doctor = Doctor(id=id, name=name, specialization=specialization)
    assert doctor.id == id
    assert doctor.name == name
    assert doctor.specialization == specialization