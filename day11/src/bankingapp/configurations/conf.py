#create confoguration file for the application
import os
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)


class Config:
    def __init__(self):
        self.connection_string = self.get_mongo_uri()
        
    
    def get_mongo_uri(self):
        app_env=os.getenv('APP_ENV')
        if app_env == 'development':
            return os.getenv('mongo_uri')
        else:
            raise ValueError("Invalid APP_ENV value. Expected 'development'.")
            