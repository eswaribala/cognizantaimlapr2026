#create customer repository abstract class

from abc import ABC, abstractmethod

class CustomerRepository(ABC):
    @abstractmethod
    def create_customer(self, customer_request):
        pass

    
    @abstractmethod
    def get_all_customers(self):
        pass
    