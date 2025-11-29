from fastapi_users.authentication import JWTStrategy
from app.core.config import settings

SECRET = f"{settings.secret_key}"
LIFETIME_SECONDS = 3600

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=LIFETIME_SECONDS)

