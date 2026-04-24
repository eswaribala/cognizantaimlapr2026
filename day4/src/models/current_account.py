#create current account class with attributes account number, account type, balance, overdraft limit
from src.models.account import Account
class CurrentAccount(Account):
    def __init__(self, account_number: int, running_total: float, date_of_opening, overdraft_limit: float):
        super().__init__(account_number, running_total, date_of_opening)
        self.__overdraft_limit = overdraft_limit

    @property
    def overdraft_limit(self):
        return self.__overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, overdraft_limit):
        self.__overdraft_limit = overdraft_limit