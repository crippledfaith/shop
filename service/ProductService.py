from model.Product import Product
from db_context.QueryContext import QueryContext
from service.CategoryService import CategoryService


class ProductService:

    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
            cls.__instance.context = QueryContext()
        return cls.__instance

    def add_product(self, obj):
        name_exits = self.context.get_all_by_condition(
            "product", {"name": obj.name}).count()
        if name_exits > 0:
            return False
        self.context.save('product', obj.__dict__)
        return True

    def update_product(self, obj):
        if obj._id != "":
            product = self.get_product(obj._id)
            if not product:
                return False
        else:
            return False
        if obj.category_id != "":
            category = CategoryService().get_category(obj.category_id)
            if not category:
                return False
        name_exits = self.context.get_all_by_condition(
            "product", {"name": obj.name}).count()
        if name_exits > 0:
            return False
        self.context.update('product', obj.__dict__)

    def delete_product(self, obj):
        if obj._id != "":
            category = self.get_product(obj._id)
            if not category:
                return False
        else:
            return False
        self.context.delete('product', obj.__dict__)

    def get_products(self, category_id):
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
