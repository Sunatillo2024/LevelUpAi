from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="LevelUpAI API")

@app.get("/")
def root():
    return {"message": "Welcome to LevelUpAI"}
