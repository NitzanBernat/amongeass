from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from src.db.mongo import get_collection, get_db_collection_names, insert, update_collection, delete_collection, \
    delete_db, delete_one
from src.db.postgres import get_db_by_name

router = APIRouter()
security = HTTPBasic()


@router.get("/read_from_collection")
def read_from_collection(db_name: str, collection_name: str):
    chack_db(db_name)
    return list(get_collection(db_name, collection_name).find())


@router.get("/read_from_database")
def read_from_database(db_name: str):
    chack_db(db_name)
    data = {}
    for collection_name in get_db_collection_names(db_name):
        data.update({collection_name: list(get_collection(db_name, collection_name).find())})
    return data


@router.put("/write_to_collection")
def write_to_collection(db_name: str, collection_name: str, data: dict):
    chack_db(db_name)
    insert(collection_name,db_name, data)


@router.post("/update_collection")
def update_collection_in_db(db_name: str, collection_name: str, old_data: dict, new_data: dict):
    chack_db(db_name)
    update_collection(db_name, collection_name, old_data, new_data)


@router.delete("/delete_collection")
def delete_collection_in_db(db_name: str, collection_name: str):
    chack_db(db_name)
    delete_collection(db_name, collection_name)


@router.delete("/delete_db")
def delete(db_name: str):
    chack_db(db_name)
    delete_db(db_name)


@router.delete("/delete_row")
def delete_row(db_name: str, collection_name: str, data: dict):
    chack_db(db_name)
    delete_one(db_name, collection_name, data)


def chack_db(db_name: str):
    if get_db_by_name(db_name) is None or get_db_by_name(db_name).get("status") == "DELETED":
        raise HTTPException(status_code=404, detail="db_name not found")
def chack2():
    pass