from fastapi import APIRouter, Depends
from crouton import SQLAlchemyCRUDRouter
from models import ItemModel, ItemCreate, Item
from db import get_db
from pydantic import create_model

router = APIRouter()

ItemUpdate = create_model(
    'ItemUpdate', 
    __base__=ItemCreate,
    __module__=__name__
)

# CRUD router using Crouton for the `Item` resource
item_router = SQLAlchemyCRUDRouter(
    schema=Item,  
    create_schema=ItemCreate,  
    update_schema=ItemUpdate,  
    db_model=ItemModel,  
    db=get_db,
    prefix='items'
)

# CRUD routes in the router
router.include_router(item_router)