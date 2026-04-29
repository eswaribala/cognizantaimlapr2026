import sys
import os
import pytest

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')
)
sys.path.insert(0, project_root)

from src.bankingapp.configurations.mongodb_conn import MongoDBConnection

def test_mongo_connection():
    mongo_client=MongoDBConnection.get_connection()
    assert mongo_client is not None, "Failed to establish MongoDB connection"   
    MongoDBConnection.close_connection()
