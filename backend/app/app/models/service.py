from typing import TYPE_CHECKING
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Service:
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(Text(length=36), default=lambda: str(uuid.uuid4()), index=True)
    description = Column(String(1000), index=True)
    price = Column(Float)
    image_url = Column(String(500))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())