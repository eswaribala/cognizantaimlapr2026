"""
write test case for doctor not found exception
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

from src.exceptions.doctor_not_found_exception import DoctorNotFoundException
from src.stores.doctorstore import DoctorStore

def test_doctor_not_found_exception():
    doctor_store = DoctorStore()
    with pytest.raises(DoctorNotFoundException):
        doctor_store.get_doctor_by_id(999)

