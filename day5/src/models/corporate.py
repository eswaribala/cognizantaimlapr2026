#create corporate class inherit from customer using pydantic
from pydantic import Field
from models.company_type import CompanyType
from models.customer import Customer
class Corporate(Customer):
    company_type: CompanyType
    registration_number: str = Field(..., description="Company Registration Number")
