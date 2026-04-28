
from pydantic import BaseModel


class ProductResponse(BaseModel):
    product_id: int
    product_name: str
    price: float
    stock_quantity: int
    catalog_id: int
