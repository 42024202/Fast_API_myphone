from pydantic import BaseModel, ConfigDict
from .brand import BrandOut
from .model import ModelOut
from .storage import StorageOut
from .color import ColorOut


class PhoneOut(BaseModel):
    id: int
    price:int
    brand:BrandOut
    model:ModelOut
    storage:StorageOut
    color:ColorOut
    condition:str
    is_active:bool
    description:str

    model_config = ConfigDict(from_attributes=True)
