import urllib.parse
import certifi
from pymongo import MongoClient

username = "vhebcompany"
password = "Xnz0gCNIvrkQg1SE"

uri = f"mongodb://{username}:{urllib.parse.quote_plus(password)}@ac-iepkg00-shard-00-00.acakwxa.mongodb.net:27017,ac-iepkg00-shard-00-01.acakwxa.mongodb.net:27017,ac-iepkg00-shard-00-02.acakwxa.mongodb.net:27017/?ssl=true&replicaSet=atlas-wcg1od-shard-0&authSource=admin&retryWrites=true&w=majority&appName=cholacluster"

client = MongoClient(
    uri,
    tls=True,
    tlsCAFile=certifi.where()
)

print(client.list_database_names())