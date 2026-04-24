#display customers data from txt file using pipeline runner
import sys
import os
from faker import Faker
# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)

from src.dataloaders.customer_json_data_loader import CustomerJSONDataLoader
from src.dataloaders.customer_csv_data_loader import CustomerCSVDataLoader
from src.configurations.conf import Config
from src.dataloaders.customer_txt_data_loader import CustomerTXTDataLoader
from src.stores.customer_store_impl import CustomerStoreImpl
from src.utils.pipeline_runner import PipelineRunner

def load_customers(**kwargs):
   config = Config()
   customer_store = kwargs['customer_store']
   env=config.app_env
   if env=="Testing":
      data_loader = CustomerTXTDataLoader()
      data_loader.load_data(config.resource_path, customer_store)
   if env=="Development":
      data_loader = CustomerCSVDataLoader()
      data_loader.load_data(config.resource_path, customer_store)
   if env=="Production":
      data_loader = CustomerJSONDataLoader()
      data_loader.load_data(config.resource_path, customer_store)
   return customer_store

def display_customers(**kwargs):
   customer_store = kwargs['customer_store']
   for customer in customer_store.get_all_customers():
         print(f"customer_id: {customer.customer_id}")
         print(f"name: {customer.name.first_name} {customer.name.last_name}")    
         print(f"email: {customer.email}")
         print(f"phone_no: {customer.phone_no}")
         print("-------------")   
   
def update_customer(**kwargs):
   customer_store = kwargs['customer_store']
   customer_id = kwargs['customer_id']
   customer=customer_store.get_customer(customer_id)
   fake = Faker()
   customer.name.first_name = fake.first_name()
   customer.name.last_name = fake.last_name()
   customer.email = fake.email()
   customer.phone_no = fake.random_int(min=1000000000, max=9999999999)
   customer_store.update_customer(customer_id, customer)
   return customer_store

def get_customer_by_id(**kwargs):   
   customer_store = kwargs['customer_store']
   customer_id = kwargs['customer_id']
   customer=customer_store.get_customer(customer_id)
   print(f"customer_id: {customer.customer_id}")
   print(f"name: {customer.name.first_name} {customer.name.last_name}")    
   print(f"email: {customer.email}")
   print(f"phone_no: {customer.phone_no}")
   print("-------------")
def delete_customer(**kwargs):
   customer_store = kwargs['customer_store']
   customer_id = kwargs['customer_id']
   customer_store.delete_customer(customer_id)
   print(f"Customer with id {customer_id} deleted successfully.")
          
if __name__ == "__main__":   
   customer_store = CustomerStoreImpl()
   pipeline_runner = PipelineRunner()
   pipeline_runner.add_stage(load_customers)
   pipeline_runner.add_stage(display_customers)
   pipeline_runner.add_stage(update_customer)
   pipeline_runner.add_stage(get_customer_by_id)
   pipeline_runner.add_stage(delete_customer)
   pipeline_runner.run(customer_store=customer_store, customer_id=1)
      