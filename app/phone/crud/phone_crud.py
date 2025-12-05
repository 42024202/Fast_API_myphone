from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from app.phone.models import Phone
from app.phone.schemas_v1.phone import PhoneCreate, PhoneUpdate

from app.phone.models import Model


class PhoneCRUD:
    async def create_phone(
            self,
            phone_in: PhoneCreate,
            session: AsyncSession
            ) -> Phone:
        phone = Phone(**phone_in.model_dump())
        session.add(phone)
        await session.commit()
        stmt = (
            select(Phone)
            .options(
                selectinload(Phone.brand),
                selectinload(Phone.model).selectinload(Model.brand),
                selectinload(Phone.battery),
                selectinload(Phone.storage),
                selectinload(Phone.screen),
                selectinload(Phone.country_of_origin),)
            .where(Phone.id == phone.id))
        result = await session.execute(stmt)
        return result.scalar_one()



    async def get_phone(self, session: AsyncSession, phone_id: int) -> Phone | None:
        stmt = (
            select(Phone)
            .options(
                selectinload(Phone.brand),
                selectinload(Phone.model).selectinload(Model.brand),
                selectinload(Phone.battery),
                selectinload(Phone.storage),
                selectinload(Phone.screen),
                selectinload(Phone.country_of_origin),)
            .where(Phone.id == phone_id))

        result = await session.execute(stmt)
        return result.scalar_one_or_none()    

    async def get_phones(self, session: AsyncSession) -> list[Phone]:
        stmnt = (
            select(Phone)
            .options(
                selectinload(Phone.brand),
                selectinload(Phone.model).selectinload(Model.brand),
                selectinload(Phone.battery),
                selectinload(Phone.storage),
                selectinload(Phone.screen),
                selectinload(Phone.country_of_origin),
            )
            .order_by(Phone.id)
        )

        result = await session.execute(stmnt)
        phones = result.scalars().all()
        
        return list(phones)

    async def patch_phone(
            self,
            session: AsyncSession,
            phone: Phone,
            phone_update: PhoneUpdate
            ):
        update_data = phone_update.model_dump(exclude_unset=True)

        for name, value in update_data.items():
            setattr(phone, name, value)

        await session.commit()
        await session.refresh(phone)
        stmt = (
            select(Phone)
            .options(
                selectinload(Phone.brand),
                selectinload(Phone.model).selectinload(Model.brand),
                selectinload(Phone.battery),
                selectinload(Phone.storage),
                selectinload(Phone.screen),
                selectinload(Phone.country_of_origin),)
            .where(Phone.id == phone.id))

        result = await session.execute(stmt)
        return result.scalar_one()


    async def delete_phone(
            self,
            session: AsyncSession,
            phone: Phone
            ):
        await session.delete(phone)
        await session.commit()

