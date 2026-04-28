
from ecommerce.dtos.catalog_request import CatalogRequest
from ecommerce.models.catalog import Catalog
from ecommerce.repository.catalog_repository import CatalogRepository
from ecommerce.configurations.mysql_conn import MySQLConnection

class CatalogRepositoryImpl(CatalogRepository):
    def create_catalog(self, catalog: CatalogRequest):
        session = MySQLConnection.get_session()
        try:
            #dto to model
            new_catalog = Catalog(
                catalog_name=catalog.catalog_name,
                description=catalog.description
            )
            session.add(new_catalog)
            session.commit()
            session.refresh(new_catalog)
            return new_catalog
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_all_catalogs(self):
        session = MySQLConnection.get_session()
        try:
            catalogs = session.query(Catalog).all()
            return catalogs
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_catalog_by_id(self, catalog_id: int):
        session = MySQLConnection.get_session()
        try:
            catalog = session.query(Catalog).filter(Catalog.catalog_id == catalog_id).first()
            return catalog
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def update_catalog(self, catalog_id: int, catalog: CatalogRequest):
        session = MySQLConnection.get_session()
        try:
            existing_catalog = session.query(Catalog).filter(Catalog.catalog_id == catalog_id).first()
            if not existing_catalog:
                return None
            
            existing_catalog.catalog_name = catalog.catalog_name
            existing_catalog.description = catalog.description
            session.commit()
            session.refresh(existing_catalog)
            return existing_catalog
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete_catalog(self, catalog_id: int):
        session = MySQLConnection.get_session()
        try:
            catalog = session.query(Catalog).filter(Catalog.catalog_id == catalog_id).first()
            if not catalog:
                return None
            session.delete(catalog)
            session.commit()
            return catalog
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()