#rceate redis client
import redis
import os
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

class RedisClient:
    def __init__(self):
        host = os.getenv("redis_host")
        port = int(os.getenv("redis_port"))        
        self.client = redis.Redis(host=host, port=port)

    def set(self, key, value):
        self.client.set(key, value)

    def get(self, key):
        return self.client.get(key)