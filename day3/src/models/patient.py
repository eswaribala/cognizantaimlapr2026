"""
create patient with id, name, dob, ailment as attributes and __str__ method to print the details of the patient
"""
import typing
from datetime import date
class Patient:
    def __init__(self, id:int, name:str, dob:date, ailment:str):
        self.id=id
        self.name=name
        self.dob=dob
        self.ailment=ailment
    def __str__(self):
        return f"Patient [id={self.id}, name={self.name}, dob={self.dob}, ailment={self.ailment}]"