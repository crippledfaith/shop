from service.product_service import product_service
from models.category import *  

#name = input("name: ")
#level = input("level: ")
#parent_id =input("parent_id")

service = product_service()
#category = category()
#category.name = name
#category.level = int(level)
#category.parent_id = parent_id
#service.add_category(category)
print(service.get_categories(0,None))