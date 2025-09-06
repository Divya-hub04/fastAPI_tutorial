from fastapi import FastAPI, Query
from enum import Enum
from typing import Optional, List

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, Gitpod World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str):
    return {"user_id": user_id, "item_id": item_id}

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    elif model_name is ModelName.lenet:
        return {"model_name": model_name, "message": "LeNet is a Classic!"}
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/search/")
async def search_items(query: str):
    return {"query": query, "results": f"Searching for '{query}'..."}

@app.get("/items/{item_id}/details")
async def read_item_details(item_id: int, q: Optional[str] = None):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/products/")
async def read_products(tags: Optional[List[str]] = Query(None)):
    return {"tags": tags}