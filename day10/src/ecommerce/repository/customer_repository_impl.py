#create customer respository implementation
from ecommerce.models.customer import Customer
from ecommerce.models.full_name import FullName
from ecommerce.repository.customer_repository import CustomerRepository
from ecommerce.configurations.mysql_conn import MySQLConnection
from datetime import datetime
class CustomerRepositoryImpl(CustomerRepository): 

    def create_customer(self, customer_request):
        session=MySQLConnection.get_session()
        #converting customer request to customer model
        #converting full name request to full name model
        full_name=FullName(
            first_name=customer_request.first_name,
            last_name=customer_request.last_name
        )
        customer=Customer(
            full_name=full_name,
            email=customer_request.email,
            password=customer_request.password,
            created_at=datetime.now(),
            updated_at=datetime.now()
            

        )
        #insert customer into database
        session.add(customer)
        #commit the transaction
        session.commit()
        #close the session
        session.close()

        return customer
