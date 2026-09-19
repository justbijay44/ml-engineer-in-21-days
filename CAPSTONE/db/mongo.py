import os
import pymongo
from datetime import datetime, timezone, timedelta

def make_connection(db_name, collection_name, uri):
    client = pymongo.MongoClient(uri)

    db = client[db_name]
    collection = db[collection_name]
    return db, collection

def insert_prediction(
        collection, transaction_id, amount, 
        hours, prediction, probability
):
    doc = {
        "transaction_id"    : transaction_id,
        "amount"            : amount,
        "hours"             : hours,
        "prediction"        : prediction,
        "probability"       : probability,
        "timestamp"         : datetime.now(timezone.utc)
    }

    collection.insert_one(doc)

def create_indexes(collection):
    collection.create_index([("prediction", 1), ("timestamp", -1)])

def check_drift(collection, hours=24, baseline=0.0017):
    cutoff_time = datetime.now(timezone.utc) - timedelta(hours=hours)

    total = collection.count_documents({
        "timestamp": {"$gte": cutoff_time}
    })

    fraud_count = collection.count_documents({
        "timestamp": {"$gte": cutoff_time},
        "prediction": "fraud"
    })

    if not total == 0:
        rate = fraud_count / total
        if rate > baseline * 2:
            return "possible drift"

    return "no drift"

def find_duplicates(collection):
    pipeline = [
        {"$group": {"_id": "$transaction_id", "count": {"$sum": 1}}},
        {"$match": {"count": {"$gt": 1}}}
    ]
    return list(collection.aggregate(pipeline))

if __name__ == "__main__":
    uri = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
    db, collection = make_connection("fraud_db", "predictions", uri)

    create_indexes(collection)

    # insert_prediction(
    #     collection, transaction_id=1, amount=149.62, hours=14.5, 
    #     prediction="fraud", probability=0.87
    # )

    hours = 24
    baseline = 0.0017

    # print(check_drift(collection, hours, baseline))
    print(find_duplicates(collection))