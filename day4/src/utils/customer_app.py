#display customers
import sys
import os
from faker import Faker

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)
from src.data_loaders.customer_data_loader import CustomerDataLoader
from src.stores.customer_store_impl import CustomerStoreImpl
from src.configurations.conf import Config

def load_and_display_customers(file_path: str):
    customer_store = CustomerStoreImpl()
    data_loader = CustomerDataLoader(file_path, customer_store)
    data_loader.load_data()
    display_customers(customer_store)

def display_customers(customer_store: CustomerStoreImpl):
    customers = customer_store.customers
    for customer_id, customer in customers.items():
        print(f"Customer ID: {customer_id}")
        print(f"Full Name: {customer.full_name.first_name} {customer.full_name.last_name}")
        print(f"Email: {customer.email}")
        print(f"Phone No: {customer.phone_no}")
        print("-" * 20)

if __name__ == "__main__":
    file_path = Config().file_path
    load_and_display_customers(file_path)
