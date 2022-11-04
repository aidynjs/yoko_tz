from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base, DateTimeMixin



class Employee(Base, DateTimeMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String, unique=True, nullable=False)
    shop_point_id = Column(Integer, ForeignKey('shop_point.id'))

    shop_point = relationship('ShopPoint', backref='employees')

