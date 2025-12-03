from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db_helpers import db_helper
from app.user.user_permissions import admin_only
from app.phone.schemas_v1.characters.battery import BatteryCreate, BatteryUpdate, BatteryOut
from app.phone.services_v1.characters_services import battery_service


router = APIRouter(prefix="/batteries", tags=["Battery"])


@router.get("/", response_model=list[BatteryOut])
async def get_batteries(
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await battery_service.battery_list(session)


@router.get("/{battery_id}", response_model=BatteryOut)
async def get_battery(
    battery_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await battery_service.get_or_404(session, battery_id)


@router.post("/", response_model=BatteryOut, dependencies=[Depends(admin_only)])
async def create_battery(
    battery_in: BatteryCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await battery_service.create(session, battery_in)


@router.put("/{battery_id}", response_model=BatteryOut, dependencies=[Depends(admin_only)])
async def update_battery(
    battery_id: int,
    battery_in: BatteryUpdate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await battery_service.update_battery(session, battery_id, battery_in)


@router.delete("/{battery_id}", dependencies=[Depends(admin_only)])
async def delete_battery(
    battery_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await battery_service.delete_battery(session, battery_id)

