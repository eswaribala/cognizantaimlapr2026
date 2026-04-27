#create customer service abstract class
from abc import ABC, abstractmethod

class CustomerService(ABC):
    @abstractmethod
    def create_customer(self, customer_data):
        pass

    @abstractmethod
    def get_all_customers(self):
        pass
    @abstractmethod
    def get_customer_by_id(self, customer_id):
        pass
    @abstractmethod
    def update_customer(self, customer_id, customer_data):
        pass

    @abstractmethod
    def delete_customer(self, customer_id):
        pass