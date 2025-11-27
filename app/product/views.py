from sqlalchemy.ext.asyncio import AsyncSession
from .crud import (create_product, get_product_by_id, get_products
)
from .schemas.schema_v1 import ProductCreate


class ProductServiceV1:
    """Business logic for products."""

    async def list_products(self, session: AsyncSession):
        return await get_products(session)

    async def get_product(self, session: AsyncSession, id: int):
        return await get_product_by_id(session, id)

    async def create_product(self, session: AsyncSession, product_in: ProductCreate):
        return await create_product(product_in, session)

