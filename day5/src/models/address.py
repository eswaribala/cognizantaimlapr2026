#create address class associate to customer using pydantic
from pydantic import BaseModel, Field
from models.customer import Customer
class Address(BaseModel):
    #associate address to customer using customer id    
    customer: Customer
    street: str = Field(..., min_length=3, max_length=100, description="Street Address")
    city: str = Field(..., min_length=2, max_length=50, description="City")
    state: str = Field(..., min_length=2, max_length=50, description="State")
    zip_code: str = Field(..., min_length=5, max_length=10, description="ZIP Code")
    country: str = Field(..., min_length=2, max_length=50, description="Country")