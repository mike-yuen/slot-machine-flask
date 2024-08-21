from os.path import dirname, join
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import as_declarative, declared_attr

from app.config import settings

SQLALCHEMY_DATABASE_URI = settings.APPLICATION_POSTGRES_URL

ssl_args = {"sslrootcert": join(dirname(__file__), "ca.pem")}

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, connect_args=ssl_args)

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
