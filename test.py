from service.ProductService import ProductService
from models.Category import Category

name = input("name: ")
level = input("level: ")
parent_id = input("parent_id")

service = ProductService()
category = Category()
category.name = name
category.level = int(level)
category.parent_id = parent_id
service.add_category(category)
print(service.get_categories(0, None))

