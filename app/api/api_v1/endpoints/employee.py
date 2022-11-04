from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api.deps import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.Employee])
def read_employees(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    return crud.employee.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=schemas.Employee)
def create_employee(
    *, db: Session = Depends(get_db), employee_in: schemas.EmployeeCreate
) -> Any:
    employee = crud.employee.create(db, obj_in=employee_in)
    return employee


@router.put("/{id}", response_model=schemas.Employee)
def update_item(
    *,
    db: Session = Depends(get_db),
    id: int,
    employee_in: schemas.EmployeeUpdate,
) -> Any:
    """
    Update an item.
    """
    employee = crud.employee.get(db=db, id=id)
    if not employee:
        raise HTTPException(status_code=404, detail="Item not found")
    employee = crud.employee.update(db=db, db_obj=employee, obj_in=employee_in)
    return employee


@router.delete("/{id}", response_model=schemas.Employee)
def delete_item(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    employee = crud.employee.get(db=db, id=id)
    if not employee:
        raise HTTPException(status_code=404, detail="Item not found")
    employee = crud.employee.remove(db=db, id=id)
    return employee
