from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class DebitBase(BaseModel):
    status: Optional[str] = None


# Properties to receive on Debit creation
class DebitCreate(DebitBase):
    pass


# Properties to receive on Debit update
class DebitUpdate(DebitBase):
    status: str


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
