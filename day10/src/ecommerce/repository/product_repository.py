
from abc import ABC,abstractmethod
from typing import List

from ecommerce.dtos.product_request import ProductRequest
from ecommerce.models.product import Product

class ProductRepository(ABC):
    @abstractmethod
    def add_product(self, product: ProductRequest) -> Product:
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def get_all_products(self) -> List[Product]:
         pass
   
    @abstractmethod
    def update_product(self, product_id: int, product: ProductRequest) -> Product:
        pass

    @abstractmethod
    def delete_product(self, product_id: int) -> bool:
        pass