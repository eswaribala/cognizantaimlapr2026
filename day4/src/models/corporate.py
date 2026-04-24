#create corporate class with attributes name, email, phone number, company type
from src.models.company_type import CompanyType
from src.models.customer import Customer
class Corporate(Customer):
    def __init__(self, customer_id: int, name: str, email: str, phone_number: str, company_type: CompanyType):
        super().__init__(customer_id, name, email, phone_number)
        self.__company_type = company_type

    @property
    def company_type(self):
        return self.__company_type

    @company_type.setter
    def company_type(self, company_type):
        self.__company_type = company_type
    