from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID

import uvicorn
from fastapi import Body, FastAPI
from typing_extensions import Annotated

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[Optional[datetime], Body()] = None,
    end_datetime: Annotated[Optional[datetime], Body()] = None,
    repeat_at: Annotated[Optional[time], Body()] = None,
    process_after: Annotated[Optional[timedelta], Body()] = None,
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
