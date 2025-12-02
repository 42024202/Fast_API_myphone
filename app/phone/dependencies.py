from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db_helpers import db_helper
from app.phone.crud.phone_crud import PhoneCRUD


phone_crud = PhoneCRUD()

async def get_phone_or_404(
    phone_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy)
):
    phone = await phone_crud.get_phone(session, phone_id)
    if not phone:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Phone not found"
        )
    return phone

