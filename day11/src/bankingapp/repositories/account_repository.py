#create account request abstract class AccountRepository:
from abc import ABC, abstractmethod

from bankingapp.dtos.account_request import AccountRequest
class AccountRepository(ABC):
    @abstractmethod
    def create_account(self, account:AccountRequest):
        pass

    @abstractmethod
    def get_account(self, account_id:int):
        pass

    @abstractmethod
    def update_account(self, account_id:int, balance:float):
        pass

    @abstractmethod
    def delete_account(self, account_id:int):
        pass