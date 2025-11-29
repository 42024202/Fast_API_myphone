from fastapi_users.authentication import AuthenticationBackend
from fastapi_users.authentication import BearerTransport
from app.core.auth import get_jwt_strategy

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

