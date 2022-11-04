from typing import Optional

from pydantic import BaseModel, validator

STATUS_LIST = ["started", "ended", "in process", "awaiting", "canceled"]


class OrderBase(BaseModel):
    shop_point_id: Optional[int]
    customer_id: Optional[int]
    status: Optional[str]
    employee_id: Optional[int]

    @validator("status")
    def check_status(cls, v, values):
        if v in STATUS_LIST:
            return v
        raise ValueError("Not right status")


class CustomerOrderCreate(BaseModel):
    employee_id: int
    status: str

    @validator("status")
    def check_status(cls, v, values):
        if v in STATUS_LIST:
            return v
        raise ValueError("Not right status")


class OrderCreate(OrderBase):
    shop_point_id: int
    customer_id: int
    status: str
    employee_id: int


class OrderUpdate(OrderBase):
    ...


class OrderInDBBase(OrderBase):
    id: int

    class Config:
        orm_mode = True


class Order(OrderInDBBase):
    pass


class OrderInDB(OrderInDBBase):
    pass
