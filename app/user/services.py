from fastapi import Depends
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, BearerTransport
from fastapi_users.db import SQLAlchemyUserDatabase
from app.user.models.user import User
from app.user.schemas.schema_v1 import UserCreate, UserUpdate, UserDB
from app.core.db_helpers import db_helper
from app.core.auth import get_jwt_strategy

async def get_user_db(session=Depends(db_helper.session_dependancy)):
    yield SQLAlchemyUserDatabase(session, User)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager=get_user_db,
    auth_backends=[auth_backend],
    user_model=User,
    user_create_model=UserCreate,
    user_update_model=UserUpdate,
    user_db_model=UserDB,
)

