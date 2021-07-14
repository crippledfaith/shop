from models.category import category
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

    def get_categories(self,level,parent_id):
        categoryList =[]
        categories=[]
        if(level==0):
            categories=self.context.get_all_by_condition("category",'{ "level":0 }')
        else:
            categories = []
        for cotegory in categories:
            categoryList.append(category(cotegory))

        return categoryList
