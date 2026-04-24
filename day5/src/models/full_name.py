#design data validation for full name
from pydantic import BaseModel, Field
class FullName(BaseModel):
    first_name: str = Field(..., pattern="^[A-Za-z]+$", description="The first name of the person")
    last_name: str = Field(..., pattern="^[A-Za-z]+$", description="The last name of the person")