from app.crud.base import CRUDBase
from app.models.order import Order
from app.schemas import OrderCreate, OrderUpdate


class CRUDOrder(CRUDBase[Order, OrderCreate, OrderUpdate]):
    ...


order = CRUDOrder(Order)
