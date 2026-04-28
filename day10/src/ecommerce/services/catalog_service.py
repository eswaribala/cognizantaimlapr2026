
from abc import ABC, abstractmethod

from ecommerce.dtos.catalog_request import CatalogRequest


class CatalogService(ABC):
    @abstractmethod
    def create_catalog(self, catalog_data:CatalogRequest):
        pass
    @abstractmethod
    def get_all_catalogs(self):
        pass
    @abstractmethod
    def get_catalog_by_id(self, catalog_id: int):
        pass
    @abstractmethod
    def update_catalog(self, catalog_id: int, catalog_data: CatalogRequest):
        pass
    @abstractmethod
    def delete_catalog(self, catalog_id: int):
        pass