from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship

from app.db.base_class import Base, DateTimeMixin


class Order(Base, DateTimeMixin):
    id = Column(Integer, primary_key=True)
    shop_point_id = Column(Integer, ForeignKey('shop_point.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))
    
    order_type = Column(Integer)

    status = Column(String, nullable=False)
    employee_id = Column(Integer, ForeignKey('employee.id'))

    shop_point = relationship('ShopPoint', backref='orders')
    customer = relationship('Customer', backref='orders')
    employee = relationship('Employee', backref='orders')

    visit = relationship('Visit', back_populates='order', uselist=False)
