from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db_helpers import db_helper
from app.user.user_permissions import admin_only
from app.phone.schemas_v1.characters.model import ModelCreate, ModelUpdate, ModelOut
from app.phone.services_v1.characters_services import model_service


router = APIRouter(prefix="/models", tags=["Model"])


@router.get("/", response_model=list[ModelOut])
async def get_models(
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await model_service.model_list(session)


@router.get("/{model_id}", response_model=ModelOut)
async def get_model(
    model_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await model_service.get_or_404(session, model_id)


@router.post("/", response_model=ModelOut, dependencies=[Depends(admin_only)])
async def create_model(
    model_in: ModelCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await model_service.create(session, model_in)


@router.put("/{model_id}", response_model=ModelOut, dependencies=[Depends(admin_only)])
async def update_model(
    model_id: int,
    model_in: ModelUpdate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await model_service.update_model(session, model_id, model_in)


@router.delete("/{model_id}", dependencies=[Depends(admin_only)])
async def delete_model(
    model_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await model_service.delete_model(session, model_id)

