#create customer service implementation class
import datetime

from ecommerce.dtos.customer_request import CustomerRequest
from ecommerce.dtos.customer_response import CustomerResponse
from ecommerce.repository.customer_repository_impl import CustomerRepositoryImpl
from ecommerce.dtos.full_name_request import FullNameRequest
from ecommerce.models.customer import Customer
from .customer_service import CustomerService

class CustomerServiceImpl(CustomerService):
    def __init__(self):
        self.customer_repository=CustomerRepositoryImpl()
    
    def create_customer(self, customer_data:CustomerRequest):
        
        
        created_customer=self.customer_repository.create_customer(customer_data)
        return CustomerResponse(
            id=created_customer.id,
            full_name=FullNameRequest(
                first_name=created_customer.first_name,
                last_name=created_customer.last_name
            ),
            email=created_customer.email,
            password=created_customer.password,
            created_at=str(created_customer.created_at),
            updated_at=str(created_customer.updated_at)
        )
    
    def get_all_customers(self):
        customers=self.customer_repository.get_all_customers()
        customer_responses=[]
        for customer in customers:
            customer_responses.append(
                CustomerResponse(
                    id=customer.id,
                    full_name=FullNameRequest(
                        first_name=customer.first_name,
                        last_name=customer.last_name
                    ),
                    email=customer.email,
                    password=customer.password,
                    created_at=str(customer.created_at),
                    updated_at=str(customer.updated_at)
                )
                
            )
        return customer_responses