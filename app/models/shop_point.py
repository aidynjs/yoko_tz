from sqlalchemy import Column, String, Integer

from app.db.base_class import Base, DateTimeMixin


class ShopPoint(Base, DateTimeMixin):
    __tablename__ = "shop_point"
    id = Column(Integer, primary_key=True)
    name = Column(String)


