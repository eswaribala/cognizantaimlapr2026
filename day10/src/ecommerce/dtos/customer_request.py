
# This file defines the CustomerRequest DTO (Data Transfer Object) for handling customer-related data in the e-commerce application.
from ecommerce.dtos.full_name_request import FullNameRequest
from pydantic import BaseModel, EmailStr, Field

class CustomerRequest(BaseModel):
    full_name: FullNameRequest
    email: EmailStr
    password: str = Field(..., example="password123", 
                          min_length=5,
                          max_length=8,
                          description="Password for the customer account")