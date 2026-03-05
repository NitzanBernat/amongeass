import datetime
from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Response, status
from src.db import Metadata
from src.db.mongo import change_db_name
from src.db.postgres import add_db, get_db_by_id, update_db_name, delete_db, get_db_by_id_with_user

router = APIRouter()
security = HTTPBasic()


@router.post("/")
def create_db(db_name: str,credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if db_name.startswith(credentials.username):
        return add_db(Metadata(db_name=db_name, status="CREATED", user=credentials.username, created_at=datetime.datetime.now()))
    else:
        raise HTTPException(status_code=404, detail="db_name must start with username")


@router.get("/{db_id}")
def get_by_id(db_id: str, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    metadata = get_db_by_id(db_id)
    if metadata.name.startswith(credentials.username):
        return metadata
    else:
        raise HTTPException(status_code=404, detail="db_name must start with username")


@router.put("/{db_id}")
def change_name(db_id: str, name: str, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if name.startswith(credentials.username):
        metadata = get_db_by_id_with_user(db_id)
        old_name = metadata.get("db_name")
        change_db_name(old_name, name)
        update_db_name(db_id, name)
    else:
        raise HTTPException(status_code=404, detail="db_name must start with username")


@router.delete("/{db_id}")
def delete_by_id(db_id: str, response: Response, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    metadata = get_db_by_id(db_id)
    if metadata.name.startswith(credentials.username):
        delete_db(db_id)
        response.status_code = status.HTTP_204_NO_CONTENT
    else:
        raise HTTPException(status_code=404, detail="db_name must start with username")


@router.get("/connection_string/{deployment_id}")
def get_connection_string(deployment_id: str, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    metadata = get_db_by_id(deployment_id)
    if metadata.name.startswith(credentials.username):
        return "mongodb://nraboy:password1234@localhost:27017/" + str(metadata.get("db_name"))
    else:
        raise HTTPException(status_code=404, detail="db_name must start with username")

def chack():
    pass
