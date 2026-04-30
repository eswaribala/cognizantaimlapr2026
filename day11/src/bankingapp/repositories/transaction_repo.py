#create transaction repository abstract class

from abc import ABC, abstractmethod

from bankingapp.dtos.transaction_request import TransactionRequest
from bankingapp.dtos.transaction_response import TransactionResponse
class TransactionRepository(ABC):
    @abstractmethod
    async def create_transaction(self, transaction:TransactionRequest)->TransactionResponse:
        pass

    @abstractmethod
    async def get_transaction_by_id(self, transaction_id:int)->TransactionResponse:
        pass

    @abstractmethod
    async def get_all_transactions(self)->list[TransactionResponse]:
        pass

    @abstractmethod
    async def update_transaction(self, transaction:TransactionRequest)->TransactionResponse:
        pass

    @abstractmethod
    async def delete_transaction(self, transaction_id:int)->bool:
        pass