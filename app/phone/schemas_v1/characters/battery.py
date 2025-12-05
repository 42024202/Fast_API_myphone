from pydantic import BaseModel, ConfigDict


class BatteryBase(BaseModel):
    capacity: int

    fast_charging: bool

    wireless_charging: bool

    charging_connector: str


class BatteryCreate(BatteryBase):
    pass


class BatteryUpdate(BaseModel):
    capacity: int | None = None

    fast_charging: bool | None = None

    wireless_charging: bool | None = None

    charging_connector: str | None = None


class BatteryOut(BatteryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

