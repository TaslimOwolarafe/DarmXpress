from app.db.base_class import Base
from .service import Service

class Cleaning(Base, Service):
    __tablename__ = "cleaning_services"