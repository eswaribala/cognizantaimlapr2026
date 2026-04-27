#create customer service implementation class
from ecommerce.dtos.customer_response import CustomerResponse
from ecommerce.repository.customer_repository_impl import CustomerRepositoryImpl
from ecommerce.dtos.full_name_request import FullNameRequest

from .customer_service import CustomerService

class CustomerServiceImpl(CustomerService):
    def __init__(self):
        self.customer_repository = CustomerRepositoryImpl()

    def to_response(self, customer):
        return CustomerResponse(
            #id=customer.id,
            name=FullNameRequest(
                first_name=customer.full_name.first_name,
                last_name=customer.full_name.last_name
            ),
            email=customer.email,
            password=customer.password
        )

    def create_customer(self, customer_data):
        #dto to entity and saving to database
        customer = self.customer_repository.create_customer(customer_data)
        print(f"Customer created with ID: {customer}")
        return customer

    def get_all_customers(self):
        #convert entities to dtos and return
        customers = self.customer_repository.get_all_customers()
        return [self.to_response(c) for c in customers]