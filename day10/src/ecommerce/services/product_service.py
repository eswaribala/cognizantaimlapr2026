
from abc import ABC, abstractmethod
from typing import List

from ecommerce.dtos.product_response import ProductResponse
from ecommerce.dtos.product_request import ProductRequest


class ProductService(ABC):
    @abstractmethod
    def get_product_by_id(self, product_id: int) -> List[ProductResponse]:
        pass

    @abstractmethod
    def list_products(self) -> List[ProductResponse]:
        pass

    @abstractmethod
    def create_product(self, product_data: ProductRequest) -> ProductResponse:
        pass

    @abstractmethod
    def update_product(self, product_id: int, product_data: ProductRequest) -> ProductResponse:
        pass

    @abstractmethod
    def delete_product(self, product_id: int) -> bool:
        pass