'''
Tworzy API z endpointem GET i POST. FastAPI generuje automatyczną dokumentację Swagger UI: http://localhost:8000/docs.
'''
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}


@app.post("/items/")
def create_item(item: Item):
    return {"received_item": item}
