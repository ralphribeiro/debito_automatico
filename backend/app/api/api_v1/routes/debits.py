from typing import Any

from app.schemas.debit import DebitCreate
from app.models.debit import Debit
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/request", response_model=schemas.Debit)
def get_automatic_debit(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Request Automatic Debit
    """
    debit = crud.debit.get_by_owner(db, owner_id=current_user.id)
    if debit:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Automatic debit request already made.")

    obj_in = DebitCreate()
    return crud.debit.create_with_owner(db, obj_in=obj_in,
                                        owner_id=current_user.id)    


# https://fastapi.tiangolo.com/tutorial/path-params/