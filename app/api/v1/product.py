from fastapi import APIRouter
from ...product.views import ProductServiceV1
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db_helpers import db_helper
from app.product.schemas.schema_v1 import ProductCreate, ProductOut


router = APIRouter(prefix="/products", tags=["Product"])

product_service = ProductServiceV1()


@router.get("/", response_model=list[ProductOut])
async def get_products(session: AsyncSession = Depends(db_helper.session_dependancy)):
    """GET all products"""
    return await product_service.list_products(session)


@router.get("/{id}/", response_model=ProductOut)
async def get_product(id: int, session: AsyncSession = Depends(db_helper.session_dependancy)):
    """GET product by id"""
    product = await product_service.get_product(session, id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {id} not found"
        )
    return product


@router.post("/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_dependancy)
):
    """CREATE product"""
    return await product_service.create_product(session, product_in)

