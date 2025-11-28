from contextlib import asynccontextmanager
from fastapi import FastAPI, Path
from .core import db_helper, Base
from .core.config import settings
from .api.v1.product import router as product_router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(product_router_v1, prefix=f"{settings.api_v1_prefix}")

