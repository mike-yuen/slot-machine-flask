from app.config.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    picture = Column(String, nullable=True)
    chip = Column(Integer, nullable=True)
