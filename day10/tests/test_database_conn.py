import sys
import os
import pytest

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')
)
sys.path.insert(0, project_root)
from ecommerce.configurations.mysql_conn import MySQLConnection
#@pytest.fixture(scope="module")
#def test_database_connection():
   # dbconn=MySQLConnection()
   # return dbconn
def test_get_connection():
    connection = MySQLConnection.get_connection()
    assert connection is not None
    MySQLConnection.close_connection(connection)
