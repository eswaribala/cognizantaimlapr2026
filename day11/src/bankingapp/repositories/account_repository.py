#create account request abstract class AccountRepository:
from abc import ABC, abstractmethod

from bankingapp.dtos.account_request import AccountRequest
class AccountRepository(ABC):
    @abstractmethod
    async def create_account(self, account:AccountRequest):
        pass

    @abstractmethod
    async def get_account(self, account_id:int):
        pass

    @abstractmethod
    async def update_account(self, account_id:int, balance:float):
        pass

    @abstractmethod
    async def delete_account(self, account_id:int):
        pass