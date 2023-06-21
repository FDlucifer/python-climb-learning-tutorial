# pip install pymongo

from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.son import SON

client = MongoClient("localhost", 27017)
db = client.neuraldb

people = db.people

people.insert_one({"name": "Mike", "age": 30})

for person in people.find():
    print(person)

print([p for p in people.find({"_id": ObjectId("134123418293741238471234")})])
print(people.count_documents({"name": "Lisa"}))

pipline = [
    {
        "$group": {
            "_id": "$name",
            "averageAge": {"$avg": "$age"}
        }
    },
    {
        "$group": SON([("averageAge", -1), ("_id", -1)])
    }
]

results = people.aggregate(pipline)

for result in results:
    print(result)
