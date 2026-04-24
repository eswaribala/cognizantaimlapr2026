#load customer data from csv file using pandas and store it in the customer store
import pandas as pd
from src.models.customer import Customer
from src.models.full_name import FullName
from src.stores.customer_store_impl import CustomerStoreImpl
class CustomerDataLoader:
    def __init__(self, file_path: str, customer_store: CustomerStoreImpl):
        self.file_path = file_path
        self.customer_store = customer_store
    def load_data(self):
        df = pd.read_csv(self.file_path)
        for _, row in df.iterrows():
            customer_id = int(row['customer_id'])
            full_name = FullName(
              first_name=row['first_name'],
              last_name=row['last_name']
            )
            email = row['email']
            phone_no = row['phone_no']
            customer = Customer(
                customer_id=customer_id,
                full_name=full_name,
                email=email,
                phone_no=phone_no,
                
            )
            self.customer_store.add_customer(customer)
    