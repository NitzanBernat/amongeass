from pymongo import MongoClient

client = MongoClient("mongodb://nraboy:password1234@localhost:27017/")


def insert(collection_name: str, db_name: str, data: dict):
    collection = get_collection(collection_name, db_name)
    collection.insert_one(data)


def delete_collection(collection_name: str, db_name: str):
    collection = get_collection(collection_name, db_name)
    collection.drop()


def delete_one(collection_name: str, db_name: str, data: dict):
    collection = get_collection(collection_name, db_name)
    collection.delete_one(data)


def update_collection(collection_name: str, db_name: str, old_data: dict, new_data: dict):
    collection = get_collection(collection_name, db_name)
    collection.update_one(old_data, new_data)


def find_db(collection_name: str, db_name: str):
    collection = get_collection(collection_name, db_name)
    return collection.find()


def get_collection(collection_name: str, db_name: str):
    db = client[db_name]
    return db[collection_name]


def change_collection_name(collection_name: str, db_name: str, collection_new_name: str):
    collection = get_collection(collection_name, db_name)
    collection.rename(collection_new_name)


def delete_db(db_name: str):
    db = client[db_name]
    for collection_name in db.list_collection_names():
        db.drop_collection(collection_name)


def change_db_name(db_name: str, new_name: str):
    db = client[str(db_name)]
    new_db = client[new_name]
    for collection_name in db.list_collection_names():
        collection = db[collection_name]
        new_collection = new_db[collection_name]
        for row in list(collection.find()):
            new_collection.insert_one(dict(row))
        db.drop_collection(collection_name)


def get_db_collection_names(db_name: str):
    db = client[db_name]
    return list(db.list_collection_names())
