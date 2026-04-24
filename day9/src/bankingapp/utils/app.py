#test mongo db connection
import sys
import os
# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)
from bankingapp.configurations.conf import Config

if __name__ == "__main__":
 config = Config()
 #create the collection
 collection=config.db.create_collection("accounts")
 #insert the document
 collection.insert_one({"account_no":1234,"balance":1000})
 print(config.db.list_collection_names())
 #show the document
 print(collection.find_one({"account_no":1234}))