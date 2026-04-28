
from fastapi import APIRouter

from ecommerce.dtos.catalog_request import CatalogRequest
from ecommerce.dtos.catalog_response import CatalogResponse
from ecommerce.services.catalog_service_impl import CatalogServiceImpl


router=APIRouter(prefix="/catalog/v1.0", tags=["catalog"])

catalog_service=CatalogServiceImpl()

@router.post("/", status_code=200,response_model=CatalogResponse)
def create_catalog(catalog_data:CatalogRequest):
    return catalog_service.create_catalog(catalog_data)

@router.get("/", status_code=200,response_model=list[CatalogResponse])
def get_all_catalogs():
    return catalog_service.get_all_catalogs()

@router.get("/{catalog_id}", status_code=200,response_model=CatalogResponse)
def get_catalog_by_id(catalog_id: int):
    return catalog_service.get_catalog_by_id(catalog_id)

@router.put("/{catalog_id}", status_code=200,response_model=CatalogResponse)
def update_catalog(catalog_id: int, catalog_data: CatalogRequest):
    return catalog_service.update_catalog(catalog_id, catalog_data)

@router.delete("/{catalog_id}", status_code=204)
def delete_catalog(catalog_id: int):
    catalog_service.delete_catalog(catalog_id)
    return {"message": "Catalog deleted successfully"}