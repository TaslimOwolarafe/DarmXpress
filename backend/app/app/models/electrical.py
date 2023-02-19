from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from .service import Service

class Electrical(Service):
    __tablename__ = "electrial_services"