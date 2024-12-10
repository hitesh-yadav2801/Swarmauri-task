from fastapi import APIRouter, Depends
from crouton import SQLAlchemyCRUDRouter
from .models import ItemModel, ItemCreate, Item  
from .db import get_db  

router = APIRouter()

# CRUD router using Crouton for the `Item` resource
item_router = SQLAlchemyCRUDRouter(
    schema=Item,
    create_schema=ItemCreate,
    db_model=ItemModel,
    db=get_db,  
    prefix='items'
)

# CRUD routes in the router
router.include_router(item_router)