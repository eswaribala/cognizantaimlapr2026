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
    
    @abstractmethod
    def get_customer_by_id(self, customer_id:int):
        pass
    @abstractmethod
    def update_customer(self, customer_id:int, customer_request:CustomerRequest):
        pass