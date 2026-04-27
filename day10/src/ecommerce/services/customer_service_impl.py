#create customer service implementation class
from ecommerce.dtos.customer_response import CustomerResponse
from ecommerce.repository.customer_repository_impl import CustomerRepositoryImpl


from .customer_service import CustomerService

class CustomerServiceImpl(CustomerService):
    def __init__(self):
        self.customer_repository = CustomerRepositoryImpl()

    def to_customer_response(self, customers):
        customer_responses = []
        for customer in customers:
            customer_response = CustomerResponse(
                id=customer.id,
                first_name=customer.full_name.first_name,
                last_name=customer.full_name.last_name,
                email=customer.email,
                created_at=customer.created_at,
                updated_at=customer.updated_at

            )
            customer_responses.append(customer_response)
        return customer_responses

    def create_customer(self, customer_data):
        #dto to entity and saving to database
        customer = self.customer_repository.create_customer(customer_data)
        return self.to_customer_response([customer])[0]

    def get_all_customers(self):
        #convert entities to dtos and return
        customers = self.customer_repository.get_all_customers()
        return self.to_customer_response(customers)