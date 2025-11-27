from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    """Base class for product."""
    name: str | None = None
    description: str | None = None
    price: int | None = None


class ProductCreate(ProductBase):
    """Class for creating product."""
    pass


class ProductOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    """Class for output product."""
    id: int
    name: str
    description: str
    price: int


class ProductUpdate(ProductBase):
    """Class for putch product."""
    pass


