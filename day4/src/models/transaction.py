#create transaction class with attributes
from datetime import datetime


class Transaction:
    def __init__(self, id:int, amount:float, time_stamp:datetime, sender:str, receiver:str, description:str  ):
        #protected attributes
        self._id = id        
        self._amount = amount
        self._time_stamp = time_stamp
        self._sender = sender
        self._receiver = receiver
        self._description = description

    @property
    def id(self):
        return self._id
   
    @id.setter
    def id(self, value):
        self._id = value
  
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def time_stamp(self):
        return self._time_stamp
    @time_stamp.setter
    def time_stamp(self, value):
        self._time_stamp = value

    @property
    def sender(self):
        return self._sender
    @sender.setter
    def sender(self, value):    
        self._sender = value 

    @property
    def receiver(self):
        return self._receiver
    @receiver.setter
    def receiver(self, value):
        self._receiver = value

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value

