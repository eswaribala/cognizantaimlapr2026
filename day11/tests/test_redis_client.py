import sys
import os
import pytest
# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')
)
sys.path.insert(0, project_root)

from src.bankingapp.configurations.redis_client import RedisClient
def test_redis_client():
    redis_client = RedisClient()
    assert redis_client is not None, "Failed to create Redis client"
    # Test set and get methods
    redis_client.set("test_key", "test_value")
    value = redis_client.get("test_key")
    assert value == "test_value", "Failed to set or get value from Redis"
