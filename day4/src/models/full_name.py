#create full name class
from pydantic import BaseModel, Field
class FullName(BaseModel):
    first_name: str = Field(..., min_length=1, description="First name of the customer")
    last_name: str = Field(..., min_length=1, description="Last name of the customer")