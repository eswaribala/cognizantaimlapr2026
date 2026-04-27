#create customer service abstract class
from abc import ABC, abstractmethod

class CustomerService(ABC):
    @abstractmethod
    def create_customer(self, customer_data):
        pass

    @abstractmethod
    def get_all_customers(self):
        pass
    