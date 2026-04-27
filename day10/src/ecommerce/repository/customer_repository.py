#create customer repository abstract class

from abc import ABC, abstractmethod

from ecommerce.dtos.customer_request import CustomerRequest

class CustomerRepository(ABC):
    @abstractmethod
    def create_customer(self, customer_request:CustomerRequest):
        pass

    
    @abstractmethod
    def get_all_customers(self):
        pass
    