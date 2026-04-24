#create account class with attributes account number, account type, balance
from datetime import date


class Account:
    def __init__(self, account_number: int, running_total: float,date_of_opening:date):
        #protected attributes
        self._account_number = account_number  
        self._running_total = running_total
        self._date_of_opening = date_of_opening

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        self._account_number = account_number

    @property
    def date_of_opening(self):
        return self._date_of_opening

    @date_of_opening.setter
    def date_of_opening(self, date_of_opening):
        self._date_of_opening = date_of_opening

    @property
    def running_total(self):
        return self._running_total

    @running_total.setter
    def running_total(self, running_total):
        self._running_total = running_total