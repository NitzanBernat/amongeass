import datetime
import enum


import sqlalchemy
from uuid import uuid4, UUID
from sqlalchemy import  Enum, DateTime
from sqlalchemy.orm import DeclarativeBase, declarative_base, sessionmaker, mapped_column, Mapped

engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/oltp_db")
metadata = sqlalchemy.MetaData()
class Base(DeclarativeBase):
  pass

Session = sessionmaker(bind=engine)
Session = Session()
class Status(enum.Enum):
    CREATED = "CREATED"
    DELETED = "DELETED"
class Metadata(Base):
    __tablename__ = "Metadata"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    db_name: Mapped[str] = mapped_column()
    status: Mapped[Enum]= mapped_column(sqlalchemy.Enum(Status))
    user: Mapped[str] = mapped_column()
    created_at: Mapped[datetime.datetime]= mapped_column(DateTime)


Base.metadata.create_all(engine)