from pydantic import BaseModel, ConfigDict


class BrandBase(BaseModel):
    """Base schema for brand"""
    name: str
    

class BrandCreate(BrandBase):
    """Schema for creating brand"""


class BrandOut(BrandBase):
    """Schema for brand"""
    id: int

    model_config = ConfigDict(from_attributes=True)

class BrandUpdate(BaseModel):
    """Schema for updating brand"""
    name: str | None

