from typing import TYPE_CHECKING
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class ServiceOrder(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, index=True)
    full_name = Column(String, index=True)
    date_created = Column(DateTime(timezone=True), server_default=func.now())
    quantity = Column(Integer, default=1)