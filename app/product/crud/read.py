from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.product import Product


async def get_products(session: AsyncSession) -> list[Product]:
    """get all products"""
    stmnt = select(Product).order_by(Product.id)
    result:Result = await session.execute(stmnt)
    products = result.scalars().all()

    return list(products)


async def get_product_by_id(session: AsyncSession, id:int)-> Product | None:
    """get product by id"""
    return await session.get(Product, id)
   
