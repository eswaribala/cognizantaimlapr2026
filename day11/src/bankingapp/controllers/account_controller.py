#create account controller 

from unittest import result

from fastapi import APIRouter


from bankingapp.dtos.account_response import AccountResponse
from bankingapp.dtos.account_request import AccountRequest
from bankingapp.services.account_service_impl import AccountServiceImpl


router=APIRouter(prefix="/accounts/v1.0",tags=["accounts"])

account_service=AccountServiceImpl()

@router.post("/",status_code=201,response_model=AccountResponse)
async def create_account(account_request: AccountRequest):
    return await account_service.create_account(account_request)
@router.get("/{account_id}",response_model=AccountResponse)
async def get_account(account_id: int):
    return await account_service.get_account(account_id)
@router.put("/{account_id}",response_model=AccountResponse)
async def update_account(account_id: int, balance: float):
    return await account_service.update_account(account_id, balance)
@router.delete("/{account_id}",status_code=204)
async def delete_account(account_id: int):
    result = await account_service.delete_account(account_id)    
    if result:
        return {"message": "Account deleted successfully"}
    else:
        return {"message": "Account not found"}