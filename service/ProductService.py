from model.Product import Product
from model.Category import Category
from db_context.QueryContext import QueryContext


class ProductService:

    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
            cls.__instance.context = QueryContext()
        return cls.__instance

    def add_category(self, obj) -> None:
        self.context.save("category", obj.__dict__)

    def add_product(self, obj):
        self.context.save('product', obj.__dict__)

    def update_category(self, obj):
        self.context.update('category', obj.__dict__)

    def update_product(self, obj):
        self.context.update('product', obj.__dict__)

    def delete_category(self, obj):
        self.context.delete('category', obj.__dict__)

    def delete_product(self, obj):
        self.context.delete('product', obj.__dict__)

    def get_categories(self, level, parent_id):
        category_list = []
        categories = []
        if level == 0:
            categories = self.context.get_all_by_condition("category", {"level": 0})
        else:
            categories = self.context.get_all_by_condition("category", {"$and": [{"level": level}, {"parent_id": parent_id}]})
        for item in categories:
            category_list.append(Category().from_dict(item))
        return category_list

    def get_products_by_category(self, category_id):
        products = []
        products_list = []
        if category_id: 
            products = self.context.get_all_by_condition('product', {'category_id': category_id})
        else:
            products = self.context.get_all('product')

        for item in products:
            products_list.append(Product().from_dict(item))
        return products_list

    def get_product(self, product_id):
        product = self.context.get_item_by_id('product', product_id)
        return Product().from_dict(product)

    def get_category(self, category_id):
        category = self.context.get_item_by_id('category', category_id)
        return Category().from_dict(category)