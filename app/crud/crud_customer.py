from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.customer import Customer
from app.schemas import CustomerCreate, CustomerUpdate


class CRUDCustomer(CRUDBase[Customer, CustomerCreate, CustomerUpdate]):
    def get_by_phone(self, db: Session, *, phone: str) -> Customer:
        return db.query(self.model).filter(Customer.phone == phone).first()


customer = CRUDCustomer(Customer)
