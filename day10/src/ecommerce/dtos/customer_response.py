#create customer response dto
# This file defines the CustomerResponse DTO (Data Transfer Object) for handling customer-related data in the e-commerce application.
from ecommerce.dtos.full_name_request import FullNameRequest
from pydantic import BaseModel, EmailStr, Field
class CustomerResponse(BaseModel):
    id: int
    full_name: FullNameRequest
    email: EmailStr
    password: str
    created_at: str
    updated_at: str