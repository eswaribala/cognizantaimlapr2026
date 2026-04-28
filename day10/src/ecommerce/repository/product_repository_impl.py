
from ecommerce.dtos.product_request import ProductRequest
from ecommerce.models.product import Product
from ecommerce.repository.catalog_repository_impl import CatalogRepositoryImpl
from ecommerce.repository.product_repository import ProductRepository
from ecommerce.configurations.mysql_conn import MySQLConnection

class ProductRespositoryImpl(ProductRepository):
    def __init__(self):
        self.catalog_repository = CatalogRepositoryImpl()

    def add_product(self, product:ProductRequest)->Product:
        # Logic to add a new product to the database
        session = MySQLConnection.get_session()
        try:
            catalog = self.catalog_repository.get_catalog_by_id(product.catalog_id)
            if not catalog:
                raise ValueError(f"Catalog with ID {product.catalog_id} does not exist.")
            
            new_product = Product(
                product_name=product.product_name,
                price=product.price,
                stock_quantity=product.stock_quantity,
                catalog_id=product.catalog_id
            )
            session.add(new_product)
            session.commit()
            session.refresh(new_product)  # Refresh to get the generated product_id
            return new_product
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    def get_product_by_id(self, product_id):
        # Logic to retrieve a product by its ID from the database
        pass

    def get_all_products(self):
        # Logic to retrieve all products from the database
        pass

    

    def update_product(self, product_id, updated_product):
        # Logic to update an existing product in the database
        pass

    def delete_product(self, product_id):
        # Logic to delete a product from the database
        pass