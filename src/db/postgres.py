from sqlalchemy import select
from sqlalchemy.orm import sessionmaker, defer

from src.db import Metadata, engine


def add_db(metadata: Metadata):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(metadata)
    db_id = metadata.id
    session.commit()
    return db_id


def delete_db(db_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    wanted_db = session.execute(select(Metadata).filter_by(id=db_id)).scalar_one()
    wanted_db.status = "DELETED"
    session.flush()
    session.commit()


def update_db_name(db_id, db_name: str):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Metadata).filter(Metadata.id == db_id).update({"db_name": db_name})
    wanted_db = session.execute(select(Metadata).filter_by(id=db_id)).scalar_one()
    wanted_db.name = db_name
    session.commit()
    session.flush()


def get_db_by_id_with_user(db_id: str):
    Session = sessionmaker(bind=engine)
    session = Session()
    wanted_rows = session.query(Metadata).filter_by(id=db_id).all()
    attributes = {}
    for row in wanted_rows:
        attributes.update({"id": row.id})
        attributes.update({"name": row.db_name})
        attributes.update({"user": row.user})
        attributes.update({"created_at": row.created_at})
        attributes.update({"status": row.status})

    session.commit()
    return attributes


def get_db_by_id(db_id: str):
    Session = sessionmaker(bind=engine)
    session = Session()
    wanted_rows = session.query(Metadata).options(defer(Metadata.user)).filter_by(id=db_id).all()
    attributes = {}
    for row in wanted_rows:
        attributes.update({"id": row.id})
        attributes.update({"name": row.db_name})
        attributes.update({"created_at": row.created_at})
        attributes.update({"status": row.status})

    session.commit()
    return attributes


def get_db_by_name(db_name: str):
    Session = sessionmaker(bind=engine)
    session = Session()
    wanted_rows = session.query(Metadata).filter_by(db_name=db_name).all()
    attributes = {}
    for row in wanted_rows:
        attributes.update({"id": row.id})
        attributes.update({"name": row.db_name})
        attributes.update({"user": row.user})
        attributes.update({"created_at": row.created_at})
        attributes.update({"status": row.status})

    session.commit()
    return attributes
