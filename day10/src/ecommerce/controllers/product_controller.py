
from fastapi import APIRouter

from ecommerce.dtos.product_request import ProductRequest
from ecommerce.dtos.product_response import ProductResponse
from ecommerce.services.product_service_impl import ProductServiceImpl


router=APIRouter(prefix="/products/v1.0", tags=["products"])
product_service=ProductServiceImpl()

@router.post("/", status_code=201, response_model=ProductResponse)
def add_product(product_data: ProductRequest):
    return product_service.add_product(product_data)

@router.get("/", status_code=200, response_model=list[ProductResponse])
def get_all_products():
    return product_service.get_all_products()
@router.get("/{product_id}", status_code=200, response_model=ProductResponse)
def get_product_by_id(product_id: int):
    return product_service.get_product_by_id(product_id)
@router.put("/{product_id}", status_code=200, response_model=ProductResponse)
def update_product(product_id: int, product_data: ProductRequest):
    return product_service.update_product(product_id, product_data)
@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int):
    product_service.delete_product(product_id)
    return {"message": "Product deleted successfully"}