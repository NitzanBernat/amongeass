import uuid
import sqlalchemy
from sqlalchemy import Column, Enum
import enum

from sqlalchemy.orm import sessionmaker, declarative_base


class Status(enum.Enum):
    CREATED = "CREATED"
    DELETED = "DELETED"
engine = sqlalchemy.create_engine("postgresql://user:password@localhost:5432/postgres",
                                  echo=True)
Session = sessionmaker(bind=engine)
Session = Session()
Base = declarative_base()
class Metadata(Base):
    __tablename__ = "Metadata"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    db_name = sqlalchemy.Column(sqlalchemy.String)
    status = sqlalchemy.Column(sqlalchemy.Enum(Status))
    created_at = sqlalchemy.Column(sqlalchemy.DateTime)
Base.metadata.create_all(engine)
