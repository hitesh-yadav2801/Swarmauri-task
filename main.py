from fastapi import FastAPI
from db import engine, get_db
from routes import router
from models import Base 


app = FastAPI()

# Create all tables in the database
Base.metadata.create_all(bind=engine)  

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# router
app.include_router(router)