#create mysql connection
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from ecommerce.configurations.conf import Config
#global base class for mysql connection
base = declarative_base()
config=Config()
engine=create_engine(
            config.conn_string,
            pool_size=10,
            max_overflow=20,
            pool_timeout=30,
            pool_recycle=1800,
            pool_pre_ping=True)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)



class MySQLConnection:
    @staticmethod
    def get_connection():
        return engine.connect()
    @staticmethod
    def get_session():
        return session_local()
    @staticmethod
    def close_connection(connection):
        connection.close()
                                    

    