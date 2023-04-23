from enum import Enum
from typing import List, Optional

import uvicorn
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing_extensions import Annotated


class Item(BaseModel):
    name: str
    description: Optional[str]
    price: float
    tax: Optional[float] = 0.0


app = FastAPI()


# @app.get("/items/")
# async def read_items(q: Annotated[Optional[str], Query(min_length=3, max_length=20, regex="^fixedquery$")] = "fixedquery"):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

@app.get("/items/")
async def read_items(q: Annotated[List[str],
                                  Query(alias="item-query",
                                        title="Query string",
                                        description="Query string for the items to search in the database that have a good match",
                                        min_length=3,
                                        deprecated=True)
                                  ] = ["foo", "bar"],
                     hidden_query: Annotated[Optional[str], Query(include_in_schema=False)] = None
                     ):
    query_items = {"q": q}
    return query_items


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
