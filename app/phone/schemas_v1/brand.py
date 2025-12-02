from pydantic import BaseModel, ConfigDict


class BrandBase(BaseModel):
    """Base schema for brand"""
    name: str
    

class BrandCreate(BrandBase):
    """Schema for creating brand"""


class BrandOut(BrandBase):
    model_config = ConfigDict(from_attributes=True)
    """Schema for brand"""
    id: int

class BrandUpdate(BaseModel):
    """Schema for updating brand"""
    name: str | None

