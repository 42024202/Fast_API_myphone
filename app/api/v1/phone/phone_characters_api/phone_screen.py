from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db_helpers import db_helper
from app.user.user_permissions import admin_only
from app.phone.schemas_v1.characters.phone_screen import PhoneScreenCreate, PhoneScreenUpdate, PhoneScreenOut
from app.phone.services_v1.characters_services import phone_screen_service


router = APIRouter(prefix="/screens", tags=["PhoneScreen"])


@router.get("/", response_model=list[PhoneScreenOut])
async def get_screens(
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await phone_screen_service.screen_list(session)


@router.get("/{screen_id}", response_model=PhoneScreenOut)
async def get_screen(
    screen_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await phone_screen_service.get_or_404(session, screen_id)


@router.post("/", response_model=PhoneScreenOut, dependencies=[Depends(admin_only)])
async def create_screen(
    screen_in: PhoneScreenCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await phone_screen_service.create(session, screen_in)


@router.put("/{screen_id}", response_model=PhoneScreenOut, dependencies=[Depends(admin_only)])
async def update_screen(
    screen_id: int,
    screen_in: PhoneScreenUpdate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await phone_screen_service.update_screen(session, screen_id, screen_in)


@router.delete("/{screen_id}", dependencies=[Depends(admin_only)])
async def delete_screen(
    screen_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await phone_screen_service.delete_screen(session, screen_id)

