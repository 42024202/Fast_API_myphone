from typing import Annotated
from fastapi import FastAPI, Path
from .items_views import router as items_router


app = FastAPI()
app.include_router(items_router)

@app.get("/")
def hello_world():
    return {
        "message": "world",
            }

