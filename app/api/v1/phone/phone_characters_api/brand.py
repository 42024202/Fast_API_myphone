from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db_helpers import db_helper
from app.user.user_permissions import admin_only
from app.phone.schemas_v1.characters import BrandCreate, BrandUpdate, BrandOut
from app.phone.services_v1.characters_services import brand_service


router = APIRouter(prefix="/brands", tags=["Brand"])


#read apies

@router.get("/", response_model=list[BrandOut])
async def get_brands(
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await brand_service.brand_list(session)


@router.get("/{brand_id}", response_model=BrandOut)
async def get_brand(
    brand_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await brand_service.get_or_404(session, brand_id)


# Create, delete, update only for admin

@router.post(
    "/",
    response_model=BrandOut,
    dependencies=[Depends(admin_only)],)

async def create_brand(
    brand_in: BrandCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await brand_service.create(session, brand_in)


@router.put(
    "/{brand_id}",
    response_model=BrandOut,
    dependencies=[Depends(admin_only)],)

async def update_brand(
    brand_id: int,
    brand_in: BrandUpdate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await brand_service.update_brand(session, brand_id, brand_in)


@router.delete(
    "/{brand_id}",
    dependencies=[Depends(admin_only)],)
async def delete_brand(
    brand_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await brand_service.delete_brand(session, brand_id)

