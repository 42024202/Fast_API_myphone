from pydantic import BaseModel, ConfigDict
from typing import Optional


class Color(BaseModel):
    name: str


class ColorCreate(Color):
    pass


class ColorUpdate(Color):
    pass


class ColorOut(Color):
    id: int

    model_config = ConfigDict(from_attributes=True)

