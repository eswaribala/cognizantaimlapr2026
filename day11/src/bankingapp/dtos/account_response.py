#create account response dto
from pydantic import BaseModel, Field
from datetime import date
from bankingapp.dtos.account_type import AccountType
class AccountResponse(BaseModel):
    account_no:int 
    account_type:AccountType
    balance:float 
    opening_date: date 