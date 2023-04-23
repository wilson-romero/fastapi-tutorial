from typing import Optional

import uvicorn
from fastapi import Cookie, FastAPI
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[Optional[str], Cookie()] = None):
    return {"ads_id": ads_id}

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
