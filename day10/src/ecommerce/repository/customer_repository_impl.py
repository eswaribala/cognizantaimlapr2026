#create customer respository implementation
from ecommerce.dtos.customer_request import CustomerRequest
from ecommerce.models.customer import Customer
from ecommerce.models.full_name import FullName
from ecommerce.repository.customer_repository import CustomerRepository
from ecommerce.configurations.mysql_conn import MySQLConnection
from datetime import datetime
class CustomerRepositoryImpl(CustomerRepository): 

     def create_customer(self, customer:CustomerRequest):
          session = MySQLConnection.get_session()
          try:
                customer=Customer(
                first_name=customer.full_name.first_name,
                last_name=customer.full_name.last_name,
                email=customer.email,
                password=customer.password,
                created_at=datetime.now(),
                updated_at= datetime.now()
            )
                session.add(customer)
                session.commit()
                session.refresh(customer)
                return customer                 
          except Exception as e:
                session.rollback()
                raise e
          finally:
                session.close()
        
     def get_all_customers(self):
          session = MySQLConnection.get_session()
          try:
                customers = session.query(Customer).all()
                return customers
          except Exception as e:
                raise e
          finally:
                session.close()