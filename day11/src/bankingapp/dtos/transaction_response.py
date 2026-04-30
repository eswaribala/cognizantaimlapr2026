#create transaction response dtofrom pydantic import BaseModel
from datetime import datetime
from pydantic import BaseModel
from bankingapp.dtos.transaction_type import TransactionType
class TransactionResponse(BaseModel):
    transaction_id:int 
    account_no:int 
    amount:float 
    transaction_type:TransactionType 
    transaction_date: str 