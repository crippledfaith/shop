from model.Cart import Cart
from model.Customer import Customer
from model.Product import Product
from model.Sale import Sale
from db_context.QueryContext import QueryContext


class CartService:
    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
            cls.__instance.context = QueryContext()
        return cls.__instance

    def create_cart(self, customer):
        cart = Cart()
        cart.sale_id = customer._id
        sale = self.context.save('sale', customer.__dict__)
        self.context.save('cart', cart.__dict__)
        return Sale().from_dict(sale)


    def add_item(self, cart, product):
        added = []
        product_id = Product()
        if cart._id != '':

        self.context.save('added', product.__dict__)



    def remove_item(self, cart, product):
        return self.context.delete('added', product.__dict__)

    def sale_confirm(self, cart):
        pass

