from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.debit import DebitCreate
from app.tests.utils.user import create_random_user


def create_debit_request(db: Session, *,
                         owner_id: Optional[int] = None) -> models.Debit:
    if not owner_id:
        user = create_random_user(db)
        owner_id = user.id
    debit_in = DebitCreate()
    return crud.debit.create_with_owner(db=db, obj_in=debit_in,
                                        owner_id=owner_id)
