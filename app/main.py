# app/main.py

from fastapi import FastAPI
from .database import SessionLocal

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
