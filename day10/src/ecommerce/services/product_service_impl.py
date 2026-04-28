
from ecommerce.dtos.product_request import ProductRequest
from ecommerce.dtos.product_response import ProductResponse
from ecommerce.models.product import Product
from ecommerce.repository.product_repository_impl import ProductRespositoryImpl
from ecommerce.services.product_service import ProductService


class ProductServiceImpl(ProductService):
    def __init__(self):
        self.product_repository = ProductRespositoryImpl()

    def get_all_products(self) -> list[ProductResponse]:
        products = self.product_repository.get_all_products()
        product_responses = []
        for product in products:
            product_responses.append(
                ProductResponse(
                    product_id=product.product_id,
                    product_name=product.product_name,
                    price=product.price,
                    stock_quantity=product.stock_quantity,
                    catalog_id=product.catalog_id
                )
            )
        return product_responses
    def get_product_by_id(self, product_id: int) -> ProductResponse:
        product = self.product_repository.get_product_by_id(product_id)
        product_response = ProductResponse(
            product_id=product.product_id,
            product_name=product.product_name,
            price=product.price,
            stock_quantity=product.stock_quantity,
            catalog_id=product.catalog_id
        )
        return product_response

    def add_product(self, product_data: ProductRequest) -> ProductResponse:
        product = self.product_repository.add_product(product_data)
        product_response = ProductResponse(
            product_id=product.product_id,
            product_name=product.product_name,
            price=product.price,
            stock_quantity=product.stock_quantity,
            catalog_id=product.catalog_id
        )
        return product_response

    def update_product(self, product_id: int, product_data: ProductRequest) -> ProductResponse:
        product = self.product_repository.update_product(product_id, product_data)
        product_response = ProductResponse(
            product_id=product.product_id,
            product_name=product.product_name,
            price=product.price,
            stock_quantity=product.stock_quantity,
            catalog_id=product.catalog_id
        )
        return product_response

    def delete_product(self, product_id: int) -> bool:
        return self.product_repository.delete_product(product_id)