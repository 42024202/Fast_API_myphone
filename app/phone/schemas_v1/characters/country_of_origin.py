from pydantic import BaseModel, ConfigDict


class CountryOfOriginBase(BaseModel):
    name: str


class CountryOfOriginCreate(CountryOfOriginBase):
    pass


class CountryOfOriginUpdate(CountryOfOriginBase):
    pass


class CountryOfOriginOut(CountryOfOriginBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
    

