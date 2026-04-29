#cerate account service implementation
from unittest import result

from bankingapp.dtos.account_request import AccountRequest
from bankingapp.dtos.account_response import AccountResponse
from bankingapp.repositories.account_repository_impl import AccountRepositoryImpl
from bankingapp.services.account_service import AccountService
from bankingapp.repositories.account_repository import AccountRepository
class AccountServiceImpl(AccountService):
    def __init__(self):
        self.account_repository = AccountRepositoryImpl()

    async def create_account(self, account_request: AccountRequest):
        result= await self.account_repository.create_account(account_request)
        account_response=AccountResponse(id=result._id, 
          account_no=result.account_no,
          account_type=result.account_type,
           balance=result.balance,
           opening_date=result.opening_date)
        return account_response
    async def get_account(self, account_id: int):
        result = await self.account_repository.get_account(account_id)
        if result:
            account_response = AccountResponse(
                id=result._id,
                account_no=result.account_no,
                account_type=result.account_type,
                balance=result.balance,
                opening_date=result.opening_date
            )
            return account_response
        return None
    async def update_account(self, account_id: int, balance: float):
        result= await self.account_repository.update_account(account_id, balance)
        if result:
            updated_account = await self.account_repository.get_account(account_id)
            account_response = AccountResponse(
                id=updated_account._id,
                account_no=updated_account.account_no,
                account_type=updated_account.account_type,
                balance=updated_account.balance,
                opening_date=updated_account.opening_date
            )
            return account_response
        return None
    async def delete_account(self, account_id: int):
        return await self.account_repository.delete_account(account_id)
