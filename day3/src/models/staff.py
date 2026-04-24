"""
create class Staff inherit from Person class and associated to role as attribute
"""
#inherit from Person class
from src.models.person import Person
from src.models.role import Role
class Staff(Person):
    """
    class Staff
    """

    def __init__(self, adharCardNo: str, mobileNo: int, role: Role):
        super().__init__(adharCardNo, mobileNo)
        #assocition with Role class
        self.__role = role
    
    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value: Role):
        self.__role = value
    