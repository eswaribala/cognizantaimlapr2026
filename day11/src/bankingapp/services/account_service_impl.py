#cerate account service implementation
from bankingapp.dtos.account_request import AccountRequest
from bankingapp.repositories.account_repository_impl import AccountRepositoryImpl
from bankingapp.services.account_service import AccountService
from bankingapp.repositories.account_repository import AccountRepository
class AccountServiceImpl(AccountService):
    def __init__(self):
        self.account_repository = AccountRepositoryImpl()

    async def create_account(self, account_request: AccountRequest):
        return await self.account_repository.create_account(account_request)
    async def get_account(self, account_id: int):
        return await self.account_repository.get_account(account_id)
    async def update_account(self, account_id: int, balance: float):
        return await self.account_repository.update_account(account_id, balance)
    async def delete_account(self, account_id: int):
        return await self.account_repository.delete_account(account_id)
