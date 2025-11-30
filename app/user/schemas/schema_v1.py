from fastapi_users import schemas
from app.user.models.user import UserRole


class UserRead(schemas.BaseUser[int]):
    role: UserRole


class UserCreate(schemas.BaseUserCreate):
    role: UserRole | None = None


class UserUpdate(schemas.BaseUserUpdate):
    role: UserRole | None = None

