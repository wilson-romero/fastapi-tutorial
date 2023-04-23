from enum import Enum
from typing import List, Optional

import uvicorn
from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel
from typing_extensions import Annotated


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str]
    price: float
    tax: Optional[float]


class User(BaseModel):
    username: str
    full_name: Optional[str]


# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     q: Optional[str] = None,
#     item: Optional[Item] = None,
#     user: Optional[User] = None,
#     importance: Annotated[int, Body(gt=0)] = 5
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     if user:
#         results.update({"user": user})
#     if importance:
#         results.update({"importance": importance})
#     return results

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=False)]):
    results = {"item_id": item_id, "item": item}
    return results

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
