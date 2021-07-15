from model.Category import Category
from db_context.QueryContext import QueryContext


class ProductService:
    def __init__(self) -> None:
        self.context = QueryContext()

    def add_category(self, obj)->None:
        self.context.save("category", obj.__dict__)

    def add_product(self, obj):
        self.context.save('product', obj.__dict__)

    def update_category(self, obj):
        self.context.update('category', obj.__dict__)

    def update_product(self, obj):
        self.context.update('product', obj.__dict__)

    def delete_category(self,obj):
        self.context.delete('category', obj.__dict__)

    def delete_product(self,obj):
        self.context.delete('product', obj.__dict__)

    def get_categories(self, level, parent_id):
        category_list = []
        categories = []
        if level == 0:
            categories = self.context.get_all_by_condition("category", {"level": 0})
        else:
            categories = []
        for item in categories:
            category_list.append(Category.from_dict(item))

        return category_list
