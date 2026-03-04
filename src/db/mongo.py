
from pymongo import MongoClient


client = MongoClient("mongodb://nraboy:password1234@localhost:27017/")

def create_db_and_collection(db_name: str, collection_name: str):
    dblist = client.list_database_names()
    if db_name not in dblist:
        db = client[db_name]
        db[collection_name]
        print(db.list_collection_names())
    else:
        print("db exsit")


def create_collection(collection_name: str, db_name: str):
    dblist = client.list_database_names()
    if db_name in dblist:
        db = client[db_name]
        collist = db.list_collection_names()
        if collection_name not in collist:
            db[collection_name]


def insert(collection_name: str, db_name: str, data: dict):
    collection = get_collection(collection_name, db_name)
    collection.insert_one(data)


def delete(collection_name: str, db_name: str, data: dict):
    collection = get_collection(collection_name, db_name)
    collection.delete_one(data)


def update(collection_name: str, db_name: str, old_data: dict, new_data: dict):
    collection = get_collection(collection_name, db_name)
    collection.update_one(old_data, new_data)


def find(collection_name: str, db_name: str):
    collection = get_collection(collection_name, db_name)
    return collection.find()


def get_collection(collection_name: str, db_name: str):
    db = client[db_name]
    return db[collection_name]
