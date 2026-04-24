#create mongo db connection
import os
import sys
from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient
import certifi

class Config:
    def __init__(self):
        self.client = MongoClient(os.getenv("conn_string"), tls=True,tlsCAFile=certifi.where())
        self.db = self.client["bankingdb"]
