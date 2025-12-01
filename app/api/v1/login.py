from fastapi import APIRouter, Depends
from fastapi_users.authentication import CookieTransport, JWTStrategy
from fastapi import HTTPException

from app.core.auth import get_access_strategy, get_refresh_strategy
from app.user.user_manager import get_user_manager
from app.user.schemas.login_credintails import LoginCredentials

router = APIRouter()


@router.post("/login")
async def login(
    credentials: LoginCredentials,
    user_manager=Depends(get_user_manager),
    access_strategy: JWTStrategy = Depends(get_access_strategy),
    refresh_strategy: JWTStrategy = Depends(get_refresh_strategy),
        ):

    user = await user_manager.authenticate(credentials)

    if user is None:
        raise HTTPException(400, "Invalid credentials")

    if not user.is_verified:
        raise HTTPException(403, "Email is not verified")

    access = await access_strategy.write_token(user)
    refresh = await refresh_strategy.write_token(user)

    return {
        "access_token": access,
        "refresh_token": refresh,
        "token_type": "bearer"
            }
