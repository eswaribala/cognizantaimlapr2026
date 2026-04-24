#create mysql connection
import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    def __init__(self):
        self.host = os.getenv("host")
        self.port = os.getenv("port")
        self.mysql_user = os.getenv("mysql_user")
        self.mysql_password = os.getenv("mysql_password")
        self.database = os.getenv("database")
        self.conn_string=self.get_connection_string()

    def get_connection_string(self):
        app_env = os.getenv("APP_ENV")
        if app_env == "development":
            return f"mysql+pymysql://{self.mysql_user}:{self.mysql_password}@{self.host}:{self.port}/{self.database}"
        else:
            raise ValueError("Invalid APP_ENV value. Expected 'development'.")
