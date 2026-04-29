#create mongo db connection
from turtle import st

import certifi
from pymongo import AsyncMongoClient


from bankingapp.configurations.conf import Config
class MongoDBConnection:
    @staticmethod
    def create_client(self):
        self.config=Config()
        self.mongo_client=AsyncMongoClient(self.config.connection_string,
                                         tls=True,tlsCAFile=certifi.where())
        self.db=self.mongo_client["bankingdb"]
        self.collection=self.db.create_collection["accounts"]

    @staticmethod
    def close_connection(self):
        self.mongo_client.close()
      

