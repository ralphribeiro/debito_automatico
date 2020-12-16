from sqlalchemy import Column, ForeignKey, Integer, String

from app.db.base_class import Base


class Debit(Base):
    """
    Debit Model class.
    """
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, index=True, default=None)
    owner_id = Column(Integer, ForeignKey("user.id"))
