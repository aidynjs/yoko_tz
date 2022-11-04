from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.visit import Visit
from app.schemas import VisitCreate, VisitUpdate


class CRUDVisit(CRUDBase[Visit, VisitCreate, VisitUpdate]):
    def order_has_visit(self, db: Session, *, order_id: int) -> bool:
        visit = db.query(Visit).filter(Visit.order_id == order_id).first()
        return visit == True


visit = CRUDVisit(Visit)
