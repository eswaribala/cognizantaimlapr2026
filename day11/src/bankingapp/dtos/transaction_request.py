#create transaction request refereces account request

from pydantic import BaseModel, Field
from bankingapp.dtos.transaction_type import TransactionType
class TransactionRequest(BaseModel):
    transaction_id:int = Field(..., example=1, description="Transaction ID")
    account_no:int = Field(..., example=1234567890, description="Account number")
    amount:float = Field(..., example=100.0, description="Transaction amount", gt=0)
    transaction_type:TransactionType = Field(..., example="DEPOSIT", description="Transaction type")
    transaction_date: str = Field(..., example="2022-01-01", description="Transaction date")