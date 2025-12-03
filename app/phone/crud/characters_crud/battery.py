from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from app.phone.models import Battery
from app.phone.schemas_v1.characters.battery import BatteryCreate, BatteryUpdate


class BatteryCRUD:

    async def create_battery(
            self,
            session: AsyncSession,
            battery_in: BatteryCreate) -> Battery:

        battery = Battery(**battery_in.model_dump())
        session.add(battery)
        await session.commit()
        await session.refresh(battery)
        return battery

    async def get_battery(
            self,
            session: AsyncSession,
            battery_id: int) -> Battery | None:

        return await session.get(Battery, battery_id)

    async def get_batteries(
            self,
            session: AsyncSession) -> list[Battery]:

        stmt = select(Battery).order_by(Battery.id)
        result: Result = await session.execute(stmt)
        batteries = result.scalars().all()
        return list(batteries)

    async def update_battery(
            self,
            session: AsyncSession,
            battery: Battery,
            battery_in: BatteryUpdate) -> Battery:

        update_data = battery_in.model_dump(exclude_unset=True)
        for name, value in update_data.items():
            setattr(battery, name, value)

        await session.commit()
        await session.refresh(battery)
        return battery

    async def delete_battery(
            self,
            session: AsyncSession,
            battery: Battery):

        await session.delete(battery)
        await session.commit()

