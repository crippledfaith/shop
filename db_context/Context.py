from pymongo import MongoClient
from random import randint


class Context:
    def __init__(self):
        self.client = MongoClient(port=27017)
        self.db = self.client.shop  #?? .shop
    
    def save(self, collection_name, obj):
        self.db[collection_name].insert_one(obj)
        return
    
    def update(self, collection_name, obj):
        self.db[collection_name].find_one_and_update({'_id':})
        return

    def delete(self, collection_name, obj):
        return

