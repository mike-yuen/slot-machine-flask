from uuid import uuid4

from app.config.db.base_class import Base
from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(String, primary_key=True, default=uuid4)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    picture = Column(String, nullable=True)
    total_chip = Column(Integer, nullable=True)


class SlotSession(Base):
    id = Column(String, primary_key=True, default=uuid4)
    result = Column(JSON, nullable=True)
    bet = Column(Integer, nullable=True)
    change = Column(Integer, nullable=True)
    user_id = Column(String, ForeignKey("user.id"))
    user = relationship("User", back_populates="slot_sessions")
