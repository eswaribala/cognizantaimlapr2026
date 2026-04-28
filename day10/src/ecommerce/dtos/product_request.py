
from pydantic import BaseModel, Field

class ProductRequest(BaseModel):
    product_name: str = Field(..., min_length=5,max_length=150,
                              description="The name of the product, must be between 5 and 150 characters.")
    price: float = Field(..., gt=0, description="The price of the product, must be greater than 0.")
    stock_quantity: int = Field(..., ge=10, description="The stock quantity of the product, must be at least 10.")
    catalog_id: int = Field(..., gt=0, description="The ID of the catalog to which the product belongs, must be greater than 0.")