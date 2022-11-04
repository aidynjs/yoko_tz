from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api.deps import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.ShopPoint])
def read_shop_points(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    return crud.shop_point.get_multi(db, skip=skip, limit=limit)


@router.get("/{id}", response_model=schemas.ShopPoint)
def read_shop_point(db: Session = Depends(get_db), *, id: int) -> Any:
    return crud.shop_point.get(db, id)


@router.post("/", response_model=schemas.ShopPoint)
def create_shop_point(
    *, db: Session = Depends(get_db), shop_point_in: schemas.ShopPointCreate
) -> Any:
    shop_point = crud.shop_point.create(db, obj_in=shop_point_in)
    return shop_point


@router.put("/{id}", response_model=schemas.ShopPoint)
def update_item(
    *,
    db: Session = Depends(get_db),
    id: int,
    shop_point_in: schemas.ShopPointUpdate,
) -> Any:
    """
    Update an item.
    """
    shop_point = crud.shop_point.get(db=db, id=id)
    if not shop_point:
        raise HTTPException(status_code=404, detail="Item not found")
    shop_point = crud.shop_point.update(db=db, db_obj=shop_point, obj_in=shop_point_in)
    return shop_point


@router.delete("/{id}", response_model=schemas.ShopPoint)
def delete_item(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    shop_point = crud.shop_point.get(db=db, id=id)
    if not shop_point:
        raise HTTPException(status_code=404, detail="Item not found")
    shop_point = crud.shop_point.remove(db=db, id=id)
    return shop_point
