
from pydantic import BaseModel, Field

class CatalogRequest(BaseModel):
    catalog_name: str=Field(..., max_length=100,description="Name of the catalog")
    description: str | None = Field(None, max_length=255,description="Description of the catalog")