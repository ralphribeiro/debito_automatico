from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import crud
from app.schemas.debit import DebitCreate, DebitUpdate
from app.tests.utils.user import create_random_user


def test_create_automatic_debit(db: Session):
    debit_in = DebitCreate()
    user = create_random_user(db)
    debit = crud.debit.create_with_owner(db=db,
                                         obj_in=debit_in, owner_id=user.id)
    assert debit.owner_id == user.id
    assert debit.status is None


def test_get_automatic_debit_by_owner_id(db: Session):
    debit_in = DebitCreate()
    user = create_random_user(db)
    debit = crud.debit.create_with_owner(db,
                                         obj_in=debit_in, owner_id=user.id)
    stored_debit = crud.debit.get_by_owner(db=db, owner_id=user.id)
    assert stored_debit
    assert debit.id == stored_debit.id
    assert debit.owner_id == user.id


def test_get_automatic_debit_by_id(db: Session):
    debit_in = DebitCreate()
    user = create_random_user(db)
    debit = crud.debit.create_with_owner(db,
                                         obj_in=debit_in, owner_id=user.id)
    stored_debit = crud.debit.get(db=db, id=debit.id)
    assert stored_debit
    assert debit.id == stored_debit.id
    assert debit.owner_id == user.id


def test_update_automatic_debit(db: Session):
    debit_in = DebitCreate()
    user = create_random_user(db)
    debit = crud.debit.create_with_owner(db=db,
                                         obj_in=debit_in, owner_id=user.id)
    status = "aprovado"
    debit_update = DebitUpdate(status=status)
    debit2 = crud.debit.update_status(db, db_obj=debit, obj_in=debit_update)
    assert debit_update.status == status
    assert debit.id == debit2.id
    assert debit.owner_id == debit2.owner_id


def test_delete_automatic_debit(db: Session):
    debit_in = DebitCreate()
    user = create_random_user(db)
    debit = crud.debit.create_with_owner(db=db,
                                         obj_in=debit_in, owner_id=user.id)
    debit2 = crud.debit.remove(db, id=debit.id)
    debit3 = crud.debit.get_by_owner(db, owner_id=debit.id)
    assert debit3 is None