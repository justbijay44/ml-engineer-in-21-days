import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["testDB"]

collection = db["testcollection"]
collection.insert_one({"hello": "world"})

print(client.list_database_names())
print(db.list_collection_names())