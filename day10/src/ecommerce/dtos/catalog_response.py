
from pydantic import BaseModel

class CatalogResponse(BaseModel):
    catalog_id: int
    catalog_name: str
    description: str | None = None
