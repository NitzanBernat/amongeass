import datetime

from src.db.mongo import change_db_name
from src.db.postgres import update_db_name, get_db_by_id_with_user, get_db_by_id
from src.db import Metadata
from src.db.mongo import insert, get_collection
from src.db.postgres import get_db_by_name, add_db

name = "matmon23_02"
db_id = "8fb0519b-dc34-429e-8a8a-62dbf69a67b0"
if name.startswith("matmon23"):
    metadata = get_db_by_id_with_user(db_id)
    old_name = metadata.get("db_name")
    change_db_name(old_name, name)
    update_db_name(db_id, name)
insert("t", "hii", {"ll": "oo"})
print(list(get_collection("first", "hii").find()))
metadata = Metadata(db_name="postgres", status="CREATED", created_at=datetime.datetime.now(), user="user1")
add_db(metadata)
print((get_db_by_name("postgres")))
def get_connection_string(deployment_id: str):
    metadata = get_db_by_id(deployment_id)
    print(metadata)
    return "mongodb://nraboy:password1234@localhost:27017/" + str(metadata.get("db_name"))
get_connection_string(db_id)

