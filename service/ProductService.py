from models.Category import category
from db_context.QueryContext import QueryContext


class ProductService:
    def __init__(self) -> None:
        self.context = QueryContext()
        
    def add_category(self, obj):
        self.context.save("category", obj.__dict__)
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

    def get_categories(self, level, parent_id):
        category_list = []
        categories = []
        if level == 0:
            categories = self.context.get_all_by_condition("category", {"level": 0})
        else:
            categories = []
        for item in categories:
            category_list.append(category.from_dict(item))

        return category_list
