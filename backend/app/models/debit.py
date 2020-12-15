from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Index

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User


class Debit(Base):
    """
    Debit Model class.
    """
    id = Column(Integer, primary_key=True, index=True)
    actived = Column(Boolean(), index=True, default=False)
    request_date = Column(DateTime, index=True)
    approval_date = Column(DateTime, index=True)
    approval_owner_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="debit")
