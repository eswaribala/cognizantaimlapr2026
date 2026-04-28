# Create app FIRST
from fastapi import FastAPI
app = FastAPI(
    title="🛒 E-commerce API",
    description="API for managing e-commerce operations",
    version="1.0.0"
)

from ecommerce.configurations.mysql_conn import base, engine

#  IMPORT MODELS FIRST (VERY IMPORTANT)
from ecommerce.models.customer import Customer  
from ecommerce.models.catalog import Catalog
#create all the tables in the database
base.metadata.create_all(bind=engine)
#make api call to the customer controller

from ecommerce.controllers import customer_controller
from ecommerce.controllers import catalog_controller

app.include_router(customer_controller.router)
app.include_router(catalog_controller.router)



