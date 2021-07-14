from dbContext.context import context


class query_context(context):

    def get_item_by_id(self,collection_name,id):
        
        return
    
    def get_all(self,collection_name):
        return context.db[collection_name]