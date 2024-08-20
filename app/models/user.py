from uuid import uuid4

from app.config.database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
)


class User(Base):
    id = Column(String, primary_key=True, default=uuid4)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    picture = Column(String, nullable=True)
    total_chip = Column(Integer, nullable=True)
