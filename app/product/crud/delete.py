from sqlalchemy.ext.asyncio import AsyncSession
from ..models.product import Product


async def delete_product(session:AsyncSession, product:Product):
    await session.delete(product)
    await session.commit()

