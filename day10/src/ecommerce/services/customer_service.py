#create customer service abstract class
from abc import ABC, abstractmethod

from ecommerce.dtos.customer_request import CustomerRequest

class CustomerService(ABC):
    @abstractmethod
    def create_customer(self, customer_data:CustomerRequest):
        pass

    @abstractmethod
    def get_all_customers(self):
        pass
    