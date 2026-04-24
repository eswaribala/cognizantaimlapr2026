#show customer details
from store.customerstore import CustomerStore
class CustomerView:
    def __init__(self, customer_store: CustomerStore):
        self.customer_store = customer_store

    def display_customers(self):
        customers = self.customer_store.get_customers()
        for customer in customers:
            print(customer)