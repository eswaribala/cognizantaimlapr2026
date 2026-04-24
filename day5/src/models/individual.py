#create class individual using pydantic
from datetime import date
from pydantic import Field
from pydantic import FieldValidator
from models.customer import Customer
from models.gender import Gender
class Individual(Customer):
    gender: Gender
    dob: date = Field(..., description="Date of Birth in YYYY-MM-DD format")

    @FieldValidator('dob')
    def validate_dob(cls, value):
        if value >= date.today():
            raise ValueError("Date of Birth must be in the past")
        age = (date.today() - value).days // 365
        if age < 18:
            raise ValueError("Individual must be at least 18 years old")
        return value   
    