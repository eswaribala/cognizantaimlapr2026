#create account controller 

from fastapi import APIRouter

from bankingapp.dtos.account_response import AccountResponse
from bankingapp.services.account_service_impl import AccountServiceImpl


router=APIRouter(prefix="/accounts/v1.0",tags=["accounts"])

account_service=AccountServiceImpl()

@router.post("/",status_code=201,response_model=AccountResponse)