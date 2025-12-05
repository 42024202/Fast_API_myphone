from pydantic import BaseModel, ConfigDict
from .brand import BrandOut


class ModelBase(BaseModel):
    name: str
    brand_id: int


class ModelCreate(ModelBase):
    pass


class ModelUpdate(BaseModel):
    name: str | None = None
    brand_id: int | None = None


class ModelOut(BaseModel):

    id: int
    name:str
    brand:BrandOut

    model_config = ConfigDict(from_attributes=True)

