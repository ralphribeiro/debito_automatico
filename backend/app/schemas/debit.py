from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class DebitBase(BaseModel):
    actived: Optional[bool] = False


# Properties to receive on Debit creation
class DebitCreate(DebitBase):
    request_date: datetime

# Properties to receive on Debit update


class DebitUpdate(DebitBase):
    approval_owner_id: int
    approval_date: datetime

# Properties shared by models stored in DB


class DebitInDBBase(DebitBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Debit(DebitInDBBase):
    pass


# Properties properties stored in DB
class DebitInDB(DebitInDBBase):
    pass
