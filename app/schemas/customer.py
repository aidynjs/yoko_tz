from typing import Optional

from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: Optional[str]
    phone: Optional[str]
    shop_point_id: Optional[int]


class CustomerCreate(CustomerBase):
    name: str
    phone: str
    shop_point_id: int


class CustomerUpdate(CustomerBase):
    ...


class CustomerInDBBase(CustomerBase):
    id: int
    name: str

    class Config:
        orm_mode = True


class Customer(CustomerInDBBase):
    pass


class CustomerInDB(CustomerInDBBase):
    pass
