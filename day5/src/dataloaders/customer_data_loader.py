#create customer data loader abstract class
from abc import ABC, abstractmethod

from src.stores.customer_store_impl import CustomerStoreImpl
class CustomerDataLoader(ABC):
    @abstractmethod
    def load_data(self, file_path, customer_store: CustomerStoreImpl):
        pass