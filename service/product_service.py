from db_context.query_context import query_context


class product_service:
    def __init__(self) -> None:
        self.context = query_context()
        
    
    def add_category(self,obj):
        self.context.save("category",obj.__dict__)
        return

    def add_product(self):
        return
    
    def update_category(self):
        return

    def update_product(self):
        return
    
    def delete_category(self):
        return

    def delete_product(self):
        return