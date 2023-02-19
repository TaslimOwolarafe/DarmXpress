from app.db.base_class import Base
from .service import Service

class Electrical(Base, Service):
    __tablename__ = "electrial_services"