#create account dto


from pydantic import BaseModel, Field
from datetime import date

from bankingapp.dtos.account_type import AccountType
class AccountRequest(BaseModel):
    account_no:int = Field(..., example=1234567890, description="Account number")
    account_type:AccountType = Field(..., example="SAVINGS", description="Account type")
    balance:float = Field(..., example=1000.0, description="Account balance", gt=0)
    opening_date: str = Field(..., example="2022-01-01", description="Account opening date")