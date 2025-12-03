from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.phone.crud.characters_crud import CountryOfOriginCRUD
from app.phone.models import CountryOfOrigin
from app.phone.schemas_v1.characters import CountryOfOriginCreate, CountryOfOriginUpdate


class CountryOfOriginService:
    def __init__(self, crud: CountryOfOriginCRUD):
        self.crud = crud

    async def create(
        self,
        session: AsyncSession,
        country_in: CountryOfOriginCreate,) -> CountryOfOrigin:

        return await self.crud.create_country(session, country_in)

    async def get_or_404(
        self,
        session: AsyncSession,
        country_id: int) -> CountryOfOrigin:

        country = await self.crud.get_country(session, country_id)
        if country is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Country of origin not found")

        return country

    async def country_list(
        self,
        session: AsyncSession) -> list[CountryOfOrigin]:

        return await self.crud.get_countries(session)

    async def update_country(
        self,
        session: AsyncSession,
        country_id: int,
        country_in: CountryOfOriginUpdate) -> CountryOfOrigin:
        country = await self.get_or_404(session, country_id)
        updated = await self.crud.update_country(session, country, country_in)

        return updated

    async def delete_country(
        self,
        session: AsyncSession,
        country_id: int):

        country = await self.get_or_404(session, country_id)
        await self.crud.delete_country(session, country)
        return {"detail": "Country of origin deleted"}


country_of_origin_service = CountryOfOriginService(CountryOfOriginCRUD())

