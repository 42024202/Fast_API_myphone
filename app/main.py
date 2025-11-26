from contextlib import asynccontextmanager
from typing import Annotated
from fastapi import FastAPI, Path
from .core import db_helper, Base
from .product.models.product import Product


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/")
def hello_world():
    return {
        "message": "world",
            }

