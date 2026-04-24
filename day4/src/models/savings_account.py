#create saving account class with attributes account number, account type, balance, interest rate
from src.models.account import Account
class SavingsAccount(Account):
    def __init__(self, account_number: int, running_total: float, date_of_opening, interest_rate: float):
        super().__init__(account_number, running_total, date_of_opening)
        self.__interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate