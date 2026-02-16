from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

@app.get("/")
def get():
    return {"hello": "hello"}