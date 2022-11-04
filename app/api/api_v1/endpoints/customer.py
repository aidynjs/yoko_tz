from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api.deps import get_db

router = APIRouter()


@router.post("/visit", response_model=schemas.Visit)
def create_visit(
    db: Session = Depends(get_db),
    *,
    customer_visit_in: schemas.CustomerVisitCreate,
    phone: str,
) -> Any:
    customer = crud.customer.get_by_phone(db, phone=phone)
    order = crud.order.get(db, id=customer_visit_in.order_id)
    if order.customer_id != customer.id:
        raise HTTPException(
            status_code=403, detail="Customer has no access to this order"
        )
    if order.status in ["ended", "canceled"]:
        raise HTTPException(status_code=403, detail="Order has finished or canceled")
    if crud.visit.order_has_visit(db, order_id=order.id):
        raise HTTPException(status_code=403, detail="Order already has visit")

    employee = crud.employee.get(db, id=customer_visit_in.employee_id)

    if employee.shop_point_id != customer.shop_point_id:
        raise HTTPException(
            status_code=403, detail="Employee has no access to this Shop Point"
        )

    visit_in = schemas.VisitCreate(
        shop_point_id=customer.shop_point_id,
        order_id=order.id,
        customer_id=customer.id,
        employee_id=employee.id,
    )
    return crud.visit.create(db, obj_in=visit_in)


@router.post("/order", response_model=schemas.Order)
def create_order(
    db: Session = Depends(get_db),
    *,
    customer_order_in: schemas.CustomerOrderCreate,
    phone: str,
) -> Any:
    customer = crud.customer.get_by_phone(db, phone=phone)

    employee = crud.employee.get(db, id=customer_order_in.employee_id)

    if employee.shop_point_id != customer.shop_point_id:
        raise HTTPException(
            status_code=403, detail="Employee has no access to this Shop Point"
        )
    order_in = schemas.OrderCreate(
        shop_point_id=customer.shop_point_id,
        customer_id=customer.id,
        status=customer_order_in.status,
        employee_id=customer_order_in.employee_id,
    )
    return crud.order.create(db, obj_in=order_in)


@router.get("/", response_model=List[schemas.Customer])
def read_customers(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    return crud.customer.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=schemas.Customer)
def create_customer(
    *, db: Session = Depends(get_db), customer_in: schemas.CustomerCreate
) -> Any:
    customer = crud.customer.create(db, obj_in=customer_in)
    return customer


@router.put("/{id}", response_model=schemas.Customer)
def update_item(
    *,
    db: Session = Depends(get_db),
    id: int,
    customer_in: schemas.CustomerUpdate,
) -> Any:
    """
    Update an item.
    """
    customer = crud.customer.get(db=db, id=id)
    if not customer:
        raise HTTPException(status_code=404, detail="Item not found")
    customer = crud.customer.update(db=db, db_obj=customer, obj_in=customer_in)
    return customer


@router.delete("/{id}", response_model=schemas.Customer)
def delete_item(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    customer = crud.customer.get(db=db, id=id)
    if not customer:
        raise HTTPException(status_code=404, detail="Item not found")
    customer = crud.customer.remove(db=db, id=id)
    return customer
