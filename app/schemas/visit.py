from typing import Optional

from pydantic import BaseModel, validator


class VisitBase(BaseModel):
    shop_point_id: Optional[int]
    customer_id: Optional[int]
    order_id: Optional[int]
    employee_id: Optional[int]


class CustomerVisitCreate(BaseModel):
    employee_id: int
    order_id: int


class VisitCreate(VisitBase):
    shop_point_id: int
    customer_id: int
    order_id: int
    employee_id: int


class VisitUpdate(VisitBase):
    ...


class VisitInDBBase(VisitBase):
    id: int

    class Config:
        orm_mode = True


class Visit(VisitInDBBase):
    pass


class VisitInDB(VisitInDBBase):
    pass
