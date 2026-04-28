from ecommerce.dtos.catalog_response import CatalogResponse
from ecommerce.services.catalog_service import CatalogService
from ecommerce.repository.catalog_repository_impl import CatalogRepositoryImpl
from ecommerce.dtos.catalog_request import CatalogRequest
class CatalogServiceImpl(CatalogService):
    def __init__(self):
        self.catalog_repository = CatalogRepositoryImpl()  # This should be set to an instance of CatalogRepository

    def create_catalog(self, catalog_data: CatalogRequest):
        return self.catalog_repository.create_catalog(catalog_data) 
    
    def get_all_catalogs(self):
        #model to dto
        catalogs=self.catalog_repository.get_all_catalogs()
        catalog_responses=[]
        for catalog in catalogs:
            catalog_responses.append(
                CatalogResponse(
                    catalog_id=catalog.catalog_id,
                    catalog_name=catalog.catalog_name,
                    description=catalog.description
                )
            )
        return catalog_responses
    
    def get_catalog_by_id(self, catalog_id: int):
        catalog = self.catalog_repository.get_catalog_by_id(catalog_id)
        if catalog:
            return CatalogResponse(
                catalog_id=catalog.catalog_id,
                catalog_name=catalog.catalog_name,
                description=catalog.description
            )
        return None
    
    def update_catalog(self, catalog_id: int, catalog_data: CatalogRequest):
        updated_catalog = self.catalog_repository.update_catalog(catalog_id, catalog_data)
        if updated_catalog:
            return CatalogResponse(
                catalog_id=updated_catalog.catalog_id,
                catalog_name=updated_catalog.catalog_name,
                description=updated_catalog.description
            )
        return None
    
    def delete_catalog(self, catalog_id: int):
        deleted_catalog = self.catalog_repository.delete_catalog(catalog_id)
        if deleted_catalog:
            return CatalogResponse(
                catalog_id=deleted_catalog.catalog_id,
                catalog_name=deleted_catalog.catalog_name,
                description=deleted_catalog.description
            )
        return None