"""
Patient Not Found Exception 
"""
class PatientNotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)