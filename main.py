from typing import List, Optional, Set

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str]
    price: float
    tax: Optional[float]
    tags: Set[str] = set()
    image: Optional[List[Image]]

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "The pretender",
                "price": 42.0,
                "tax": 3.2,
                "tags": ["rock", "metal", "bar"],
                "image": [
                    {
                        "url": "http://example.com/baz.jpg",
                        "name": "The Foo live"
                    },
                    {
                        "url": "http://example.com/dave.jpg",
                        "name": "The Baz"
                    }
                ]
            }
        }


class Offer(BaseModel):
    name: str
    description: Optional[str]
    price: float
    items: List[Item]


@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    for image in images:
        print(image.url)
        print(image.name)
    return images


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
