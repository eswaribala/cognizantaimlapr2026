#create connection with cosmosdb emulator
from azure.cosmos import CosmosClient, PartitionKey, exceptions
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
endpoint = "https://localhost:8081"
key = "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=="
client = CosmosClient(endpoint, key, connection_verify=False)
# create database
database_name = 'TestDB'
database = client.create_database_if_not_exists(id=database_name)
# create container
container_name = 'TestContainer'
container = database.create_container_if_not_exists(
    id=container_name,
    partition_key=PartitionKey(path="/id"),
    offer_throughput=400
)
# insert item
item = {
    'id': '1',
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}
container.create_item(body=item)
print("Item inserted successfully.")