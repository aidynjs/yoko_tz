from app.crud.base import CRUDBase
from app.models.shop_point import ShopPoint
from app.schemas import ShopPointCreate, ShopPointUpdate


class CRUDShopPoint(CRUDBase[ShopPoint, ShopPointCreate, ShopPointUpdate]):
    ...


shop_point = CRUDShopPoint(ShopPoint)

