#external debit.py

from datetime import date, datetime

from src.models.transaction import Transaction

class ExternalDebit(Transaction):
    def __init__(self, id:int, amount:float, time_stamp:datetime, sender:str, receiver:str, description:str,branch_name:str, branch_code:str, branch_postal_code:str):
        super().__init__(id, amount, time_stamp, sender, receiver, description)
        self.__branch_name = branch_name
        self.__branch_code = branch_code
        self.__branch_postal_code = branch_postal_code
    @property
    def branch_name(self):
        return self.__branch_name
    @branch_name.setter
    def branch_name(self, value):
        self.__branch_name = value
    @property
    def branch_code(self):
        return self.__branch_code
    @branch_code.setter
    def branch_code(self, value):
        self.__branch_code = value
    @property
    def branch_postal_code(self):
        return self.__branch_postal_code
    @branch_postal_code.setter
    def branch_postal_code(self, value):
        self.__branch_postal_code = value
    
    