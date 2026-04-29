#create mongo db connection
from turtle import st

import certifi
from pymongo import AsyncMongoClient


from bankingapp.configurations.conf import Config
config=Config()
mongo_client=AsyncMongoClient(config.connection_string,
                                         tls=True,tlsCAFile=certifi.where())
db=mongo_client["bankingdb"]
collection=db.create_collection["accounts"]
class MongoDBConnection:
   
    @staticmethod 
    def get_connection():
        return mongo_client
    @staticmethod
    def close_connection():
        mongo_client.close()
      

