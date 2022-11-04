from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.employee import Employee
from app.schemas import EmployeeCreate, EmployeeUpdate


class CRUDEmployee(CRUDBase[Employee, EmployeeCreate, EmployeeUpdate]):
    def get_by_phone(self, db: Session, *, phone: str) -> Employee:
        return db.query(self.model).filter(Employee.phone == phone).first()


employee = CRUDEmployee(Employee)
