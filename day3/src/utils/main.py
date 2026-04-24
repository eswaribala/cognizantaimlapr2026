import sys
import os
from faker import Faker

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)
from src.models.person import Person
from src.models.role import Role
from src.models.staff import Staff

from conf.logger_conf import setup_logger
logger = setup_logger("main.log")

def create_person():
    """
    Create a person instance and print its details.
    """
    person = Person(adharCardNo="1234-5678-9012", mobileNo=9876543210)
    print(f"Person created with Adhar Card No: {person.adharCardNo} and Mobile No: {person.mobileNo}")
    """
      update mobile number and print the updated details
    """   
    faker = Faker()
    try:
        person.mobileNo = faker.random_number(digits=6)
        logger.info(f"Updated Mobile No: {person.mobileNo}")
    except ValueError as e:
        logger.error(f"Error updating mobile number: {e}")
    

def create_staff():
    """
    Create a staff instance and print its details.
    """  
    role = Role(name="Manager", description="Manages team and projects")
    staff = Staff(adharCardNo="9876-5432-1098", mobileNo=1234567890, role=role)
    print(f"Staff created with Adhar Card No: {staff.adharCardNo}, Mobile No: {staff.mobileNo}, Role: {staff.role.name}")


if __name__ == "__main__":
    create_person()
    create_staff()