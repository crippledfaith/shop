from db_context.Context import Context


class QueryContext(Context):
    def __init__(self):
        super().__init__()

    def get_item_by_id(self, collection_name, item_id):
        return
    
    def get_all(self, collection_name):
        return self.db[collection_name]
    
    def get_all_by_condition(self, collection_name, query):
        return self.db[collection_name].find(query)