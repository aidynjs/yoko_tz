from enum import unique
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship
from app.db.base_class import Base, DateTimeMixin


class Customer(Base, DateTimeMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String, unique=True, nullable=False)
    shop_point_id = Column(Integer, ForeignKey('shop_point.id'))
    
    shop_point = relationship('ShopPoint', backref='customers')
