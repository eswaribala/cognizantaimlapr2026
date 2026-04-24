#create json data loder to store 
import pandas as pd
from src.models.customer import Customer
from src.models.full_name import FullName
from src.dataloaders.customer_data_loader import CustomerDataLoader
from src.stores.customer_store_impl import CustomerStoreImpl
class CustomerJSONDataLoader(CustomerDataLoader):
     def load_data(self, file_path, customer_store: CustomerStoreImpl):
        df = pd.read_json(file_path)
        for _, row in df.iterrows():
            customer_id = int(row['customer_id'])
            first_name = row['first_name']
            last_name = row['last_name']
            email = row['email']
            phone_no = str(row['phone_no'])

            full_name = FullName(
                first_name=first_name,
                last_name=last_name
            )

            customer = Customer(
                customer_id=customer_id,
                name=full_name,
                email=email,
                phone_no=phone_no
            )

           

            customer_store.add_customer(customer)