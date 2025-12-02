from fastapi import APIRouter, Depends
from app.user.user_permissions import admin_only

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/panel")
async def admin_panel(user = Depends(admin_only)):
    return {"status": "ok", "message": "Welcome admin"}

