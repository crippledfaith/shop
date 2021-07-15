from service.ProductService import ProductService
from model.Category import Category
from model.Product import Product
from db_context. QueryContext import QueryContext


def add_category():
    name = input("Category name: ")
    level = input("level: ")
    parent_id = input("parent_id: ")

    service = ProductService()
    category = Category()
    category.name = name
    category.level = int(level)
    category.parent_id = parent_id
    service.add_category(category)
    print(service.get_categories(0, None))


def add_products():
    category_id = input('category id: ')
    name = input("name: ")
    unit = input('unit: ')
    mrp = input('mrp: ')
    price = input('price: ')
    tag = input('tag: ')
    service = ProductService()
    product = Product()
    product.category_id = category_id
    product.name = name
    product.unit = unit
    product.mrp = mrp
    product.price = price
    product.tag = tag
    service.add_product(product)
    add_category()


def update_products():
    _id = input('id: ')
    name = input('new name: ')
    category_id = input('category id: ')
    price = input('new price: ')
    mrp = input('new mrp: ')
    unit = input('unit: ')
    tag = input('tag: ')
    service = ProductService()
    product = Product()
    product._id = _id
    product.name = name
    product.category_id = category_id
    product.unit = unit
    product.price = price
    product.tag = tag
    service.update_product(product)


update_products()
