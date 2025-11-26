from pydantic import BaseModel


class ProductBase(BaseModel):
    """Base class for product."""
    name: str
    description: str
    price: int


class ProductCreate(ProductBase):
    """Class for creating product."""
    pass

class ProductOut(ProductBase):
    """Class for output product."""
    id: int
