from enum import Enum
from typing import Any

from app.schemas.debit import DebitCreate, DebitUpdate
from fastapi import APIRouter, Depends, HTTPException
from fastapi import status as sts
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


class StatusRequest(str, Enum):
    canceled = "canceled"
    approved = "approved"
    rejected = "rejected"


@router.get("/request", response_model=schemas.Debit)
async def get_automatic_debit(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Request Automatic Debit.
    """
    debit = crud.debit.get_by_owner(db, owner_id=current_user.id)
    if debit:
        raise HTTPException(status_code=sts.HTTP_400_BAD_REQUEST,
                            detail="Automatic debit request already made.")

    obj_in = DebitCreate()
    return crud.debit.create_with_owner(db, obj_in=obj_in,
                                        owner_id=current_user.id)


@router.put("/{debit_id}", response_model=schemas.Debit)
async def update_status(
    debit_id: int,
    status: StatusRequest,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update Automatic Debit Status.
    """
    debit = crud.debit.get(db, id=debit_id)
    print(debit)
    if not debit:
        raise HTTPException(status_code=sts.HTTP_404_NOT_FOUND,
                            detail="Not Found automatic debit request by id")

    obj_in = DebitUpdate(status=status)
    # if status_in == StatusRequest.canceled:

    debit_out = crud.debit.update_status(db, db_obj=debit, obj_in=obj_in)
    return debit_out


@router.get("/{owner_id}", response_model=schemas.Debit)
async def get_automatic_debit_by_owner_id(
    owner_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Get Automatic Debit By Owner Id.
    """
    debit = crud.debit.get_by_owner(db, owner_id=owner_id)
    if not debit:
        raise HTTPException(status_code=sts.HTTP_404_NOT_FOUND,
                            detail="Automatic debit request not found.")
    return debit
