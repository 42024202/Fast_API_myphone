from pydantic import BaseModel, ConfigDict


class PhoneScreenBase(BaseModel):
    display_name: str

    display_size: float

    refresh_rate: int


class PhoneScreenCreate(PhoneScreenBase):
    pass


class PhoneScreenUpdate(BaseModel):
    display_name: str | None = None

    display_size: float | None = None

    refresh_rate: int | None = None


class PhoneScreenOut(PhoneScreenBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

