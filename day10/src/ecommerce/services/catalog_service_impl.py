from ecommerce.services.catalog_service import CatalogService
from ecommerce.repository.catalog_repository_impl import CatalogRepositoryImpl
from ecommerce.dtos.catalog_request import CatalogRequest
class CatalogServiceImpl(CatalogService):
    def __init__(self):
        self.catalog_repository = CatalogRepositoryImpl()  # This should be set to an instance of CatalogRepository

    def create_catalog(self, catalog_data: CatalogRequest):
        return self.catalog_repository.create_catalog(catalog_data) 
    
    def get_all_catalogs(self):
        return self.catalog_repository.get_all_catalogs()
    
    def get_catalog_by_id(self, catalog_id: int):
        return self.catalog_repository.get_catalog_by_id(catalog_id)
    
    def update_catalog(self, catalog_id: int, catalog_data: CatalogRequest):
        return self.catalog_repository.update_catalog(catalog_id, catalog_data)
    
    def delete_catalog(self, catalog_id: int):
        return self.catalog_repository.delete_catalog(catalog_id)