#create address class with attributes street, city, state, zip code
#associate address with customer class

class Address:
    def __init__(self, street: str, city: str, state: str, zip_code: str):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__customer = None

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, street):
        self.__street = street

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    @property
    def zip_code(self):
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        self.__zip_code = zip_code