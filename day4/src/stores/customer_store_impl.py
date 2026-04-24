#customer store implementation
from src.models.customer import Customer
from src.stores.customer_store import CustomerStore
class CustomerStoreImpl(CustomerStore):
    def __init__(self):
        self.customers = {}
    def add_customer(self, customer: Customer):
        self.customers[customer.customer_id] = customer
    def get_customer(self, customer_id: int):
        return self.customers.get(customer_id)
    def update_customer(self, customer_id: int, customer: Customer):
        if customer_id in self.customers:
            self.customers[customer_id] = customer
    def delete_customer(self, customer_id: int):
        if customer_id in self.customers:
            del self.customers[customer_id]