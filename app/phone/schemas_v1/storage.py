from pydantic import BaseModel, ConfigDict


class StorageBase(BaseModel):
    size: int


class StorageCreate(StorageBase):
    pass


class StorageUpdate(StorageBase):
    pass


class StorageOut(StorageBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

