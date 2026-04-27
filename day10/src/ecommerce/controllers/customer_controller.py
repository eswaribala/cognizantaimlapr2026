
from fastapi import APIRouter

from ecommerce.services import customer_service
from ecommerce.services.customer_service_impl import CustomerServiceImpl

# This is a placeholder for the customer controller. 
# You can add your endpoints here.
router = APIRouter(prefix="/customers/v1.0", tags=["customers"])
#connecting the service to the controller
customer_service = CustomerServiceImpl()

@router.post("/")
def create_customer(customer_data: dict):
    return customer_service.create_customer(customer_data)

@router.get("/")
def get_customers():
    return customer_service.get_all_customers()

