from typing import Any, Dict, Optional, Union, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.debit import Debit
from app.schemas.debit import DebitCreate, DebitUpdate


class CRUDDebit(CRUDBase[Debit, DebitCreate, DebitUpdate]):
    def create_with_owner(self, db: Session, *, obj_in: DebitCreate,
                          owner_id: int) -> Debit:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_owner(self, db: Session, *, owner_id: int) -> Optional[Debit]:
        return db.query(Debit).filter(Debit.owner_id == owner_id).first()

    def update_status(self, db: Session, *,
                      db_obj: Debit,
                      obj_in: Union[DebitUpdate, Dict[str, Any]]) -> Debit:

        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=obj_in)

    def get_multi(self, db: Session, *,
                  skip: int = 0, limit: int = 100) -> List[Dict]:
        return (db.query(self.model).offset(skip).limit(limit).all())


debit = CRUDDebit(Debit)
