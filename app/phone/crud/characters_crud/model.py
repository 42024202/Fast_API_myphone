from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.engine import Result

from app.phone.models import Model
from app.phone.schemas_v1.characters.model import ModelCreate, ModelUpdate


class ModelCRUD:

    async def create_model(
                self,
                session: AsyncSession,
                model_in: ModelCreate
            ) -> Model:

        model = Model(**model_in.model_dump())
        session.add(model)
        await session.commit()
        stmt = select(Model).options(selectinload(Model.brand)).where(Model.id == model.id)
        result = await session.execute(stmt)
        return result.scalar_one() 


    async def get_model(
                self,
                session: AsyncSession,
                model_id: int
            ) -> Model | None:
        
        stmt = select(Model).options(selectinload(Model.brand)).where(Model.id == model_id)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_models(
                self,
                session: AsyncSession
            ) -> list[Model]:

        stmt = select(Model).options(selectinload(Model.brand)).order_by(Model.id)
        result: Result = await session.execute(stmt)
        models = result.scalars().all()
        return list(models)

    async def update_model(
                self,
                session: AsyncSession,
                model: Model,
                model_in: ModelUpdate
            ) -> Model:

        update_data = model_in.model_dump(exclude_unset=True)

        for name, value in update_data.items():
            setattr(model, name, value)

        await session.commit()
        stmt = select(Model).options(selectinload(Model.brand)).where(Model.id == model.id)
        result: Result = await session.execute(stmt)
        return result.scalar_one()

        
    async def delete_model(
                self,
                session: AsyncSession,
                model: Model
            ):

        await session.delete(model)
        await session.commit()

