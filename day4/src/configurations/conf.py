#create config based on env variables
import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    def __init__(self):
        self.source = os.getenv('data_source')
        print("Loaded source:", self.source)
        self.file_path=self.get_file_path() 

    def get_file_path(self):
        if self.source == 'csv':
            return 'src/resources/customers.csv'
        elif self.source == 'json':
            return 'src/resources/customers.json'
        else:
            raise ValueError('Unsupported data source')