#data validator for full name request
from pydantic import BaseModel, Field   
class FullNameRequest(BaseModel):
    first_name: str = Field(..., example="John",min_length=3, 
                            max_length=50,pattern="^[a-zA-Z]+$",
                            description="First name must be between " \
                            "3 and 50 characters and contain only letters.")
    last_name: str = Field(..., example="Doe", min_length=3, 
                           max_length=50,pattern="^[a-zA-Z]+$",
                           description="Last name must be between " \
                           "3 and 50 characters and contain only letters.")