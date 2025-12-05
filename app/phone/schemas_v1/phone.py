from pydantic import BaseModel, ConfigDict
from .characters.brand import BrandOut
from .characters.model import ModelOut
from .characters.storage import StorageOut
from .characters.country_of_origin import CountryOfOriginOut
from .characters.phone_screen import PhoneScreenOut
from .characters.battery import BatteryOut
from app.phone.models.phone import Condition
from typing import Optional


class PhoneBase(BaseModel):
    price:int
    brand_id:int
    model_id:int
    battery_id:int
    storage_id:int
    screen_id:int
    oc_version:str
    cpu:str
    cpu_cores:int
    cpu_frequency:int
    gpu:str
    ram:int
    condition:Condition
    release_year:int
    is_active:bool
    description:str
    country_of_origin_id:int
 

class PhoneCreate(PhoneBase):
    pass


class PhoneUpdate(BaseModel):
    price:int | None = None
    brand_id:int | None = None
    model_id:int | None = None
    battery_id:int | None = None
    storage_id:int | None = None
    screen_id:int | None = None
    oc_version:str | None = None
    cpu:str | None = None
    cpu_cores:int | None = None
    cpu_frequency:int | None = None
    gpu:str | None = None
    ram:int | None = None
    condition:Condition | None = None
    release_year:int | None = None
    is_active:bool | None = None
    description:str | None = None
    country_of_origin_id:int | None = None


class PhoneOut(BaseModel):
    id:int
    price:int
    brand:BrandOut
    model:ModelOut
    battery:BatteryOut
    storage:StorageOut
    screen:PhoneScreenOut
    oc_version:str
    cpu:str
    cpu_cores:int
    cpu_frequency:int
    gpu:str
    ram:int
    condition:Condition
    release_year:int
    is_active:bool
    description:str
    country_of_origin:CountryOfOriginOut

    model_config = ConfigDict(from_attributes=True)



class PhoneFilter(BaseModel):
    brand_id: Optional[int] = None
    model_id: Optional[int] = None

    price_from: Optional[int] = None
    price_to: Optional[int] = None

    ram_from: Optional[int] = None
    ram_to: Optional[int] = None

    storage_id: Optional[int] = None

    condition: Optional[str] = None 

    release_year_from: Optional[int] = None
    release_year_to: Optional[int] = None

    search: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

