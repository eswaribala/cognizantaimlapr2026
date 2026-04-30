#create transaction repository implementation
from fastapi import HTTPException
from bankingapp.dtos.transaction_response import TransactionResponse
from bankingapp.dtos.transaction_request import TransactionRequest
from bankingapp.repositories.account_repository_impl import AccountRepositoryImpl
from bankingapp.repositories.transaction_repo import TransactionRepository
from bankingapp.configurations.mongodb_conn import db,transactions_collection,MongoDBConnection

class TransactionRepoImpl(TransactionRepository):
    def __init__(self):
        self.client = MongoDBConnection.get_connection()
        self.db = db
        self.transactions_collection = transactions_collection
        self.account_repo = AccountRepositoryImpl()
    
    async def create_transaction(self, transaction:TransactionRequest)->TransactionResponse:
        account = await self.account_repo.get_account(transaction.account_no)
        if not account:
            raise HTTPException(status_code=500, detail="Account not found")
           
        
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
    
    async def get_transaction_by_id(self, transaction_id:int)->TransactionResponse:
        transaction = await self.transactions_collection.find_one({"transaction_id": transaction_id})
        if not transaction:
            raise HTTPException(status_code=500, detail="Transaction not found")
        transaction_response = TransactionResponse(
            transaction_id=transaction["transaction_id"],
            account_no=transaction["account_no"],
            amount=transaction["amount"],
            transaction_type=transaction["transaction_type"],
            transaction_date=transaction["transaction_date"]
        )
        return transaction_response
    async def get_all_transactions(self)->list[TransactionResponse]:
        transactions_cursor = self.transactions_collection.find()
        transactions = []
        async for transaction in transactions_cursor:
            transaction_response = TransactionResponse(
                transaction_id=transaction["transaction_id"],
                account_no=transaction["account_no"],
                amount=transaction["amount"],
                transaction_type=transaction["transaction_type"],
                transaction_date=transaction["transaction_date"]
            )
            transactions.append(transaction_response)
        return transactions
    async def update_transaction(self, transaction:TransactionRequest)->TransactionResponse:
        result = await self.transactions_collection.update_one(
            {"transaction_id": transaction.transaction_id},
            {"$set": {
                "account_no": transaction.account_no,
                "amount": transaction.amount,
                "transaction_type": transaction.transaction_type,
                "transaction_date": transaction.transaction_date
            }}
        )
        if result.matched_count == 0:
            raise HTTPException(status_code=500, detail="Transaction not found")
        updated_transaction = await self.transactions_collection.find_one({"transaction_id": transaction.transaction_id})
        transaction_response = TransactionResponse(
            transaction_id=updated_transaction["transaction_id"],
            account_no=updated_transaction["account_no"],
            amount=updated_transaction["amount"],
            transaction_type=updated_transaction["transaction_type"],
            transaction_date=updated_transaction["transaction_date"]
        )
        return transaction_response
    
    async def delete_transaction(self, transaction_id:int)->bool:
        result = await self.transactions_collection.delete_one({"transaction_id": transaction_id})
        return result.deleted_count > 0

 
    