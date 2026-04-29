#create mongo db connection
from turtle import st

import certifi
from pymongo import AsyncMongoClient

from bankingapp.configurations.conf import Config
config=Config()
mongo_client=AsyncMongoClient(config.connection_string,
                                         tls=True,tlsCAFile=certifi.where())
db=mongo_client["bankingdb"]
accounts_collection=db["accounts"]
transactions_collection=db["transactions"]
class MongoDBConnection:
   
    @staticmethod 
    def get_connection():
        return mongo_client
    @staticmethod
    def close_connection():
        mongo_client.close()
      

