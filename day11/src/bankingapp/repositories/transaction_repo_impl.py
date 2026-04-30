#create transaction repository implementation
from bankingapp.dtos.transaction_response import TransactionResponse
from bankingapp.dtos.transaction_request import TransactionRequest
from bankingapp.repositories.account_repository_impl import AccountRepositoryImpl
from bankingapp.repositories.transaction_repo import TransactionRepo
from bankingapp.configurations.mongodb_conn import MongoDBConnection

class TransactionRepoImpl(TransactionRepo):
    def __init__(self):
        self.client = MongoDBConnection.get_connection()
        self.db = MongoDBConnection.db
        self.transactions_collection = MongoDBConnection.transactions_collection
        self.account_repo = AccountRepositoryImpl()
    
    async def create_transaction(self, transaction:TransactionRequest)->TransactionResponse:
        account = await self.account_repo.get_account(transaction.account_no)
        if not account:
            raise ValueError("Account not found")
           
        
        transaction_doc = {
            "transaction_id": transaction.transaction_id,
            "account_no": transaction.account_no,
            "amount": transaction.amount,
            "transaction_type": transaction.transaction_type,
            "transaction_date": transaction.transaction_date
        }
        await self.transactions_collection.insert_one(transaction_doc)
        created_transaction = await self.transactions_collection.find_one({"transaction_id": transaction.transaction_id})
        transaction_response = TransactionResponse(
            transaction_id=created_transaction["transaction_id"],
            account_no=created_transaction["account_no"],
            amount=created_transaction["amount"],
            transaction_type=created_transaction["transaction_type"],
            transaction_date=created_transaction["transaction_date"]
        )
        return transaction_response

 
    