from uuid import uuid4

from app.config.database import Base
from sqlalchemy import (
    JSON,
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship


class SlotSession(Base):
    id = Column(String, primary_key=True, default=uuid4)
    result = Column(JSON, nullable=True)
    bet = Column(Integer, nullable=True)
    change = Column(Integer, nullable=True)
    user_id = Column(String, ForeignKey("user.id"))
    user = relationship("User", back_populates="slot_sessions")
