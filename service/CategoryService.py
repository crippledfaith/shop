from model.Category import Category
from db_context.QueryContext import QueryContext


class CategoryService:

    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
            cls.__instance.context = QueryContext()
        return cls.__instance

    def add_category(self, obj):
        if obj.parent_id != "":
            category = self.get_category(obj.parent_id)
            if category is None:
                return False
        name_exits = self.context.get_all_by_condition(
            "category", {"name": obj.name}).count()
        if name_exits > 0:
            return False
        self.context.save("category", obj.__dict__)
        return True

    def update_category(self, obj):
        if obj._id != "":
            category = self.get_category(obj._id)
            if category is None:
                return False
        else:
            return False
        if obj.parent_id != "":
            category = self.get_category(obj.parent_id)
            if category is None:
                return False
        self.context.update('category', obj.__dict__)
        return True

    def delete_category(self, obj):
        if obj._id != "":
            category = self.get_category(obj._id)
            if category is None:
                return False
        else:
            return False
        self.context.delete('category', obj.__dict__)
        return True

    def get_categories(self, level, parent_id):
        category_list = []
        categories = []
        if level == 0:
            categories = self.context.get_all_by_condition(
                "category", {"level": 0})
        else:
            categories = self.context.get_all_by_condition(
                "category", {"$and": [{"level": level}, {"parent_id": parent_id}]})
        for item in categories:
            category_list.append(Category().from_dict(item))
        return category_list

    def get_category(self, category_id):
        category = self.context.get_item_by_id('category', category_id)
        return Category().from_dict(category)
