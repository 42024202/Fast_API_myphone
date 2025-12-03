from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db_helpers import db_helper
from app.user.user_permissions import admin_only
from app.phone.schemas_v1.characters.storage import StorageCreate, StorageUpdate, StorageOut
from app.phone.services_v1.characters_services import storage_service


router = APIRouter(prefix="/storages", tags=["Storage"])


@router.get("/", response_model=list[StorageOut])
async def get_storages(
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await storage_service.storage_list(session)


@router.get("/{storage_id}", response_model=StorageOut)
async def get_storage(
    storage_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await storage_service.get_or_404(session, storage_id)


@router.post("/", response_model=StorageOut, dependencies=[Depends(admin_only)])
async def create_storage(
    storage_in: StorageCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await storage_service.create(session, storage_in)


@router.put("/{storage_id}", response_model=StorageOut, dependencies=[Depends(admin_only)])
async def update_storage(
    storage_id: int,
    storage_in: StorageUpdate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await storage_service.update_storage(session, storage_id, storage_in)


@router.delete("/{storage_id}", dependencies=[Depends(admin_only)])
async def delete_storage(
    storage_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await storage_service.delete_storage(session, storage_id)

