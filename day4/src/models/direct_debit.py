#direct debit class which inherits from transaction class
from datetime import date, datetime
from src.models.transaction import Transaction
class DirectDebit(Transaction):
    def __init__(self, id:int, amount:float, time_stamp:datetime, sender:str, receiver:str, description:str, payment_date:date):
        super().__init__(id, amount, time_stamp, sender, receiver, description)
        self._payment_date = payment_date
   

    @property
    def payment_date(self):
        return self._payment_date
    @payment_date.setter
    def payment_date(self, value):
        self._payment_date = value

    