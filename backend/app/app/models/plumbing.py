from app.db.base_class import Base
from .service import Service

class Plumbing(Base, Service):
    __tablename__ = "plumbing_services"