from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User


class Debit(Base):
    """
    Debit Model class.
    """
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, index=True, default=None)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User")
