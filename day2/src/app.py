# creating entry point for the application
import faker
from store.customerstore import CustomerStore
from view.customerview import CustomerView
"""
This is the main entry point for the application. It imports the faker library and defines a function called check() that creates an instance of the Faker class and prints a fake name. The if __name__ == "__main__": block ensures that the check() function is only called when this script is run directly, and not when it is imported as a module in another script.
call the customer store and customer view to display the customers
"""


def check():
    """
    This function creates an instance of the Faker class and prints a fake name. The Faker library is used to generate fake data, such as names, addresses, and phone numbers, which can be useful for testing and development purposes.
    invoke customer store and customer view to display the customers
    """
    customer_store = CustomerStore(num_customers=100)
    customer_view = CustomerView(customer_store)
    customer_view.display_customers()
    


if __name__ == "__main__":
    check()
