from fastapi import FastAPI
import models
from database import engine

app = FastAPI()


@app.get("/")
def get():
    return {"hello": "hello"}

models.Base.metadata.create_all(bind = engine)