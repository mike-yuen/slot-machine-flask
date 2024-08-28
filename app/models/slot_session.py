from app.config.database import Base
from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class SlotSession(Base):
    id = Column(Integer, primary_key=True)
    result = Column(JSON, nullable=True)
    bet = Column(Integer, nullable=True)
    change = Column(Integer, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="slot_sessions")
