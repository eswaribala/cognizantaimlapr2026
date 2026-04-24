"""
Person model definition.
"""
import re
class Person:
    """
    A class representing a person with a name and age.
    """
    def __init__(self, adharCardNo: str, mobileNo: int):
        #private attributes
        self.__adharCardNo = adharCardNo
        self.__mobileNo = mobileNo

    #getter for adharCardNo
    @property
    def adharCardNo(self):
        return self.__adharCardNo
    # getter for mobileNo
    @property
    def mobileNo(self):
        return self.__mobileNo 

    # setter for mobileNo
    @mobileNo.setter    
    def mobileNo(self, value):
        if not re.match(r'^\d{10}$', str(value)):
            raise ValueError("Mobile number must be a 10-digit number.")
        self.__mobileNo = value
    



   