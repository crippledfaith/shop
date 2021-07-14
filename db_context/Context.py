from pymongo import MongoClient
from random import randint


class Context:
    def __init__(self):
        self.client = MongoClient(port=27017)
        self.db = self.client.shop
    
    def save(self, collection_name, obj):
        self.db[collection_name].insert_one(obj)
        return
    
    def update(self, collection_name, obj):
        return

    def delete(self, collection_name, obj):
        return