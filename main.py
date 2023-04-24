
from typing import Optional, Set

import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str]
    price: float
    tax: Optional[float]
    tags: Set[str] = set()


# @app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED, tags=["items"], summary="Create an item",
#           description="Create an item with all the information, name, description, price, tax and a set of unique tags")
@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED, tags=["items"], summary="Create an item",
          response_description="The created item")
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]

@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
