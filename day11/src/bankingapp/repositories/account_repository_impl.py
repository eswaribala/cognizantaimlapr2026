#create account repository implementation
from bankingapp.repositories.account_repository import AccountRepository
from bankingapp.configurations.mongodb_conn import MongoDBConnection,db,accounts_collection
class AccountRepositoryImpl(AccountRepository):
    def __init__(self):
        self.mongo_client = MongoDBConnection.get_connection()
        self.db = db   
        self.accounts_collection = accounts_collection
    def create_account(self, account):
       account_doc={
            "account_no": account.account_no,
            "account_type": account.account_type,
            "balance": account.balance,
            "opening_date": account.opening_date
        }
       self.accounts_collection.insert_one(account_doc)
       #find account by account number
       created_account = self.accounts_collection.find_one({"account_no": account.account_no})
       return created_account
    
    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def update_account(self, account_id, balance):
        if account_id in self.accounts:
            self.accounts[account_id].balance = balance

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]