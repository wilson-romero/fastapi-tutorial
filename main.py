from typing import List, Optional

import uvicorn
from fastapi import FastAPI, Header
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[Optional[str], Header()] = None,
                     strange_header: Annotated[Optional[str], Header(
                         convert_underscores=False)] = None,
                     x_token: Annotated[Optional[List[str]], Header()] = None):
    return {"User-Agent": user_agent,
            "strange_header": strange_header,
            "X-Token values": x_token}

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
