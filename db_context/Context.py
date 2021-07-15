from pymongo import MongoClient


class Context:
    def __init__(self):
        self.client = MongoClient(port=27017)
        self.db = self.client.shop

    def save(self, collection_name, obj):
        self.db[collection_name].insert_one(obj)

    def update(self, collection_name, obj):
        self.db[collection_name].find_one_and_update({"_id": obj["_id"]}, {"$set": obj}, upsert=True)

    def delete(self, collection_name, obj):
        self.db[collection_name].delete_one({"_id": obj["_id"]})

