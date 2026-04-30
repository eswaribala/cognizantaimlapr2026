#create confoguration file for the application
import os

from dotenv import load_dotenv
import hvac
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)


class Config:
    def __init__(self):
        self.connection_string = self.get_mongo_uri()
        
    
    def get_mongo_uri(self):
        app_env=os.getenv('APP_ENV')
        root_token=os.getenv('root_token')
        if app_env == 'development':
            client = hvac.Client(
                url="http://localhost:8200",
                token=root_token       # dev token
            )
            response = client.secrets.kv.v1.read_secret(
                path="mongoatlassecret",
                mount_point="secret"
            )
            mongo_uri = response["data"]["uri"]
            return mongo_uri
            #return os.getenv('mongo_uri')
        else:
            raise ValueError("Invalid APP_ENV value. Expected 'development'.")
            