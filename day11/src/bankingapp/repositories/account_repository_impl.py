#create account repository implementation
from bankingapp.repositories.account_repository import AccountRepository
from bankingapp.configurations.mongodb_conn import MongoDBConnection,db,accounts_collection
class AccountRepositoryImpl(AccountRepository):
    def __init__(self):
        self.mongo_client = MongoDBConnection.get_connection()
        self.db = db   
        self.accounts_collection = accounts_collection
    async def create_account(self, account):
       account_doc={
            "account_no": account.account_no,
            "account_type": account.account_type,
            "balance": account.balance,
            "opening_date": account.opening_date
        }
       await self.accounts_collection.insert_one(account_doc)
       #find account by account number
       created_account = await self.accounts_collection.find_one({"account_no": account.account_no})
       return created_account
    
    async def get_account(self, account_number):
        account = await self.accounts_collection.find_one({"account_no": account_number})
        return account

    async def update_account(self, account_id, balance):
        await self.accounts_collection.update_one(
            {"account_no": account_id},
            {"$set": {"balance": balance}}
        )

    async def delete_account(self, account_number):
        result = await self.accounts_collection.delete_one({"account_no": account_number})
        return result.deleted_count > 0