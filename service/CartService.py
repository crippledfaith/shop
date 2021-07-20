from model.Cart import Cart
from model.Customer import Customer
from model.Product import Product
from model.Sale import Sale
from db_context.QueryContext import QueryContext
from model.SaleItem import SaleItem


class CartService:
    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
            cls.__instance.context = QueryContext()
        return cls.__instance

    def create_cart(self, customer):
        cart = Cart()
        sale = Sale()
        cart.sale_id = sale._id
        sale.customer_id = customer._id
        sale = self.context.save('sale', sale.__dict__)
        self.context.save('cart', cart.__dict__)
        return sale

    def add_item(self, cart, product, quantity, discount):
        sale_item = SaleItem()
        sale_item.sale_id = cart.sale_id
        sale_item.item_id = product._id
        sale_item.price = product.price
        sale_item.quantity = quantity
        sale_item.discount = discount
        self.context.save('sale_item', sale_item.__dict__)
        return sale_item

    def remove_item(self, sale_item_id):
        sale_item = SaleItem()
        sale_item._id = sale_item_id
        self.context.delete('sale_item', sale_item.__dict__)
        return None

    def sale_confirm(self, cart):
        pass

