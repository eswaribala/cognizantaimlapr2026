from ecommerce.configurations.mysql_conn import base
from sqlalchemy import Column, Integer, String
class Catalog(base):
    __tablename__ = 'catalog'
    catalog_id = Column(Integer, primary_key=True, autoincrement=True)
    catalog_name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)