#create customer model

from src.models.full_name import FullName
from pydantic import BaseModel, Field

class Customer(BaseModel):
    customer_id: int = Field(...,gt=0,description="Unique identifier for the customer")
    full_name: FullName
    email: str = Field(..., pattern=r'^\S+@\S+\.\S+$', description="Email address of the customer")
    phone_no: int = Field(...,  ge=1000000000,
        le=9999999999,description="Phone number of the customer")
