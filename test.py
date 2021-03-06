from service.ProductService import ProductService
from model.Category import Category
from model.Product import Product
from db_context. QueryContext import QueryContext
from helper.CommonHelper import CommonHelper
from service.CustomerService import CustomerService
from model.Customer import Customer
from model.Sale import Sale
from service.CartService import CartService
from model.Cart import Cart


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


def update_products():
    return


def get_product():
    id = input('id: ')
    service = ProductService()
    print(service.get_product(id).__dict__)


def add_customer():
    name = input('name: ')
    email = input('email: ')
    password = input('password: ')
    service = CustomerService()
    customer = Customer()
    customer.name = name
    customer.email = email
    customer.password = password
    service.add_customer(customer)


def update_customer():
    id = input('id: ')
    name = input('name:')
    email = input('email: ')
    password = input('password: ')
    service = CustomerService()
    customer = Customer()
    customer._id = id
    customer.name = name
    customer.email = email
    customer.password = password
    service.update_customer(customer)


def get_all_customers():
    service = CustomerService()
    print(CommonHelper.objlist_to_dict(service.get_customers()))


def delete_customer():
    id = input('Id: ')
    service = CustomerService()
    customer = Customer()
    customer._id = id
    service.delete_customer(customer)


def get_customer():
    id = input('id: ')
    service = CustomerService()
    print(service.get_customer(id).__dict__)


# service = CartService()
# cart = Cart()
# sale = Sale()
# sale.customer_id = 'a3ca102a-8190-4d97-a2e8-63fb72264304'
# service.create_cart(sale)
#

get_product()