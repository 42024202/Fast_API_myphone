from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.product import Product
from ..schemas.schema_v1 import ProductUpdate


async def putch_product(session:AsyncSession, product_update:ProductUpdate, product:Product):
    """Create product"""
    for name, value in product_update.model_dump(exclude_unset=True):
       setattr(product, name, value)
       await session.commit()
       return product

