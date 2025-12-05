from pydantic import BaseModel, ConfigDict


class Stock(BaseModel):
    phone_id: int
    color_id: int
    quantity: int


class StockCreate(Stock):
    pass


class StockUpdate(BaseModel):
    phone_id: int | None = None
    color_id: int | None = None
    quantity: int | None = None


class StockOut(Stock):
    id: int

    model_config = ConfigDict(from_attributes=True)
