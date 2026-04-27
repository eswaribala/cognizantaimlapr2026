
from fastapi import APIRouter

from ecommerce.dtos.customer_request import CustomerRequest
from ecommerce.dtos.customer_response import CustomerResponse
from ecommerce.services import customer_service
from ecommerce.services.customer_service_impl import CustomerServiceImpl

# This is a placeholder for the customer controller. 
# You can add your endpoints here.
router = APIRouter(prefix="/customers/v1.0", tags=["customers"])
#connecting the service to the controller
customer_service = CustomerServiceImpl()

@router.post("/", status_code=201, response_model=CustomerResponse)
def create_customer(customer_data: CustomerRequest):
    return customer_service.create_customer(customer_data)

@router.get("/", status_code=200, response_model=list[CustomerResponse])
def get_customers():
    return customer_service.get_all_customers()

