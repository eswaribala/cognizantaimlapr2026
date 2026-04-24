#create customer class using pydantic

from pydantic import BaseModel, Field,EmailStr
from src.models.full_name import FullName

class Customer(BaseModel):
    customer_id: int = Field(..., gt=0, description="The unique identifier for the customer")
    name: FullName
    email: EmailStr = Field(..., description="The email address of the customer")
    phone_no: int = Field(..., ge=1000000000, le=9999999999, description="The phone number of the customer")
    