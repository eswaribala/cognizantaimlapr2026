#individual class Individual:
from datetime import date

from src.models.customer import Customer
from src.models.gender import Gender


class Individual(Customer):
    def __init__(self, customer_id: int, name: str, email: str, phone_number: str, gender: Gender, dob: date):
        super().__init__(customer_id, name, email, phone_number)
        self.__gender = gender
        self.__dob = dob

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, dob):
        self.__dob = dob    