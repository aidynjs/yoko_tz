from typing import Optional

from pydantic import BaseModel


class EmployeeBase(BaseModel):
    name: Optional[str]
    phone: Optional[str]
    shop_point_id: Optional[int]


class EmployeeCreate(EmployeeBase):
    name: str
    phone: str
    shop_point_id: int


class EmployeeUpdate(EmployeeBase):
    ...


class EmployeeInDBBase(EmployeeBase):
    id: int
    name: str

    class Config:
        orm_mode = True


class Employee(EmployeeInDBBase):
    pass


class EmployeeInDB(EmployeeInDBBase):
    pass

