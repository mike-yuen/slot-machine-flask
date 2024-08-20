from app.config import settings
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from typing import Any


SQLALCHEMY_DATABASE_URI = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@as_declarative()
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @event.listens_for(SessionLocal, "before_commit")
# def before_commit(session):
#     handle_before_commit(session)
