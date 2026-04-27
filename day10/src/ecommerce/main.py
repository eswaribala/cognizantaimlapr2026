from ecommerce.configurations.mysql_conn import base, engine

#  IMPORT MODELS FIRST (VERY IMPORTANT)
from ecommerce.models.customer import Customer  
#create all the tables in the database
base.metadata.create_all(bind=engine)
#make api call to the customer controller
from fastapi import FastAPI
from ecommerce.controllers import customer_controller
app = FastAPI()
app.include_router(customer_controller.router)
