from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

Base = declarative_base()

# SQLAlchemy model
class ItemModel(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)

# Pydantic models
class ItemBase(BaseModel):
    name: str
    price: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: Optional[int] = None
    
    # Pydantic v2 configuration
    model_config = ConfigDict(from_attributes=True)