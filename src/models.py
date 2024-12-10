from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

# SQLAlchemy model
class ItemModel(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)

# Pydantic model 
class ItemCreate(BaseModel):
    name: str
    price: float

class Item(ItemCreate):
    id: int

    class Config:
        orm_mode = True