from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db_helpers import db_helper
from app.user.user_permissions import admin_only
from app.phone.schemas_v1.characters.country_of_origin import CountryOfOriginCreate, CountryOfOriginUpdate, CountryOfOriginOut
from app.phone.services_v1.characters_services import country_of_origin_service


router = APIRouter(prefix="/countries", tags=["CountryOfOrigin"])


@router.get("/", response_model=list[CountryOfOriginOut])
async def get_countries(
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await country_of_origin_service.country_list(session)


@router.get("/{country_id}", response_model=CountryOfOriginOut)
async def get_country(
    country_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await country_of_origin_service.get_or_404(session, country_id)


@router.post("/", response_model=CountryOfOriginOut, dependencies=[Depends(admin_only)])
async def create_country(
    country_in: CountryOfOriginCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await country_of_origin_service.create(session, country_in)


@router.put("/{country_id}", response_model=CountryOfOriginOut, dependencies=[Depends(admin_only)])
async def update_country(
    country_id: int,
    country_in: CountryOfOriginUpdate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await country_of_origin_service.update_country(session, country_id, country_in)


@router.delete("/{country_id}", dependencies=[Depends(admin_only)])
async def delete_country(
    country_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):

    return await country_of_origin_service.delete_country(session, country_id)

