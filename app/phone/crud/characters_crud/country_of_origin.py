from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from app.phone.models import CountryOfOrigin
from app.phone.schemas_v1.characters.country_of_origin import CountryOfOriginCreate, CountryOfOriginUpdate


class CountryOfOriginCRUD:

    async def create_country(
            self,
            session: AsyncSession,
            country_in: CountryOfOriginCreate) -> CountryOfOrigin:

        country = CountryOfOrigin(**country_in.model_dump())
        session.add(country)
        await session.commit()
        await session.refresh(country)
        return country

    async def get_country(
            self,
            session: AsyncSession,
            country_id: int) -> CountryOfOrigin | None:

        return await session.get(CountryOfOrigin, country_id)

    async def get_countries(
            self,
            session: AsyncSession) -> list[CountryOfOrigin]:

        stmt = select(CountryOfOrigin).order_by(CountryOfOrigin.id)
        result: Result = await session.execute(stmt)
        countries = result.scalars().all()
        return list(countries)

    async def update_country(
            self,
            session: AsyncSession,
            country: CountryOfOrigin,
            country_in: CountryOfOriginUpdate) -> CountryOfOrigin:

        update_data = country_in.model_dump(exclude_unset=True)
        for name, value in update_data.items():
            setattr(country, name, value)

        await session.commit()
        await session.refresh(country)
        return country

    async def delete_country(
            self,
            session: AsyncSession,
            country: CountryOfOrigin):

        await session.delete(country)
        await session.commit()

