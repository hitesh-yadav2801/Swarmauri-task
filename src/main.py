from fastapi import FastAPI
from src.db import engine, get_db
from src.routes import router
from src.models import Base 

app = FastAPI()

# Create all tables in the database
Base.metadata.create_all(bind=engine)  

# router
app.include_router(router)