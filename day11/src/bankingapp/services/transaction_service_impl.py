#create transaction service implementation from transaction service abstract class
from bankingapp.dtos.transaction_request import TransactionRequest
from bankingapp.dtos.transaction_response import TransactionResponse
from bankingapp.repositories.transaction_repo_impl import TransactionRepoImpl
from bankingapp.services.transaction_service import TransactionService
class TransactionServiceImpl(TransactionService):
    def __init__(self):
        self.transaction_repo = TransactionRepoImpl()
    
    async def create_transaction(self, transaction:TransactionRequest)->TransactionResponse:
        return await self.transaction_repo.create_transaction(transaction)
    
    async def get_transaction(self, transaction_id:int)->TransactionResponse:
        return await self.transaction_repo.get_transaction_by_id(transaction_id)
    
    async def get_all_transactions(self)->list[TransactionResponse]:
        return await self.transaction_repo.get_all_transactions()
    
    async def update_transaction(self, transaction:TransactionRequest)->TransactionResponse:
        return await self.transaction_repo.update_transaction(transaction)
    
    async def delete_transaction(self, transaction_id:int)->bool:
        return await self.transaction_repo.delete_transaction(transaction_id)