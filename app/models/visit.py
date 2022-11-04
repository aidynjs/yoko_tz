from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.db.base_class import Base, DateTimeMixin


class Visit(Base, DateTimeMixin):
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    order_id = Column(Integer, ForeignKey('order.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))
    shop_point_id = Column(Integer, ForeignKey('shop_point.id'))

    order = relationship("Order", back_populates='visit')
