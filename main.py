from enum import Enum
from typing import List, Optional

import uvicorn
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing_extensions import Annotated


app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1, le=1000)],
    q: Annotated[Optional[str], Query(alias="item-query")] = None,
    size: Annotated[float, Query(gt=0, lt=10.5)] = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
