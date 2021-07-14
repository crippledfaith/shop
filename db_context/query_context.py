from db_context.context import context


class query_context(context):
    def __init__(self):
        super().__init__()

    def get_item_by_id(self,collection_name,id):
        return
    
    def get_all(self,collection_name):
        return self.db[collection_name]
    
    def get_all_by_condition(self,collection_name,query):
        return self.db[collection_name].find(query)
