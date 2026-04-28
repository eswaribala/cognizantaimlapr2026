from ecommerce.configurations.mysql_conn import base
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
class Product(base):
    __tablename__ = 'product'
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(255), nullable=False,index=True)
    price = Column(Float, nullable=False, index=True)
    stock_quantity = Column(Integer, nullable=False)
    catalog_id = Column(ForeignKey('catalog.catalog_id'), Integer,  nullable=False)
    catalog= relationship('Catalog', back_populates='products')

   