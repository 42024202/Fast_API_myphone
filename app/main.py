from contextlib import asynccontextmanager
from fastapi import FastAPI, Path
from fastapi_users import FastAPIUsers
from .core import db_helper, Base
from .core.config import settings
from .api.v1.product import router as product_router_v1
from app.user.services import get_user_db , fastapi_users



@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(product_router_v1, prefix=f"{settings.api_v1_prefix}")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)

app.include_router(
    fastapi_users.get_register_router(),
    prefix="/auth",
    tags=["auth"]
)

app.include_router(
    fastapi_users.get_users_router(),
    prefix="/users",
    tags=["users"]
)
