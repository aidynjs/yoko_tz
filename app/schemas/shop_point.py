from typing import Optional
from pydantic import BaseModel



class ShopPointBase(BaseModel):
    name: str


class ShopPointCreate(ShopPointBase):
    ...


class ShopPointUpdate(ShopPointBase):
    ...


class ShopPointInDBBase(ShopPointBase):
    id: int
    name: str

    class Config:
        orm_mode = True


class ShopPoint(ShopPointInDBBase):
    ...


class ShopPointInDB(ShopPointInDBBase):
    ...


