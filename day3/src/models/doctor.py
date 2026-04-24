"""
define a Doctor class with id, name, and specialization attributes. Include a __str__ method for easy string representation of the Doctor object.
"""
import typing
class Doctor:
    def __init__(self, id:int, name:str, specialization:str):
        self.id = id
        self.name = name
        self.specialization = specialization
    
    def __str__(self):
        return f"Doctor(id={self.id}, name='{self.name}', specialization='{self.specialization}')"
    
        