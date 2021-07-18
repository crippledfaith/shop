from model.Cart import Cart
from model.Customer import Customer
from model.Product import Product
from db_context.QueryContext import QueryContext

class CartService:
    
    __instance = None
    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
            cls.__instance.context = QueryContext()
        return cls.__instance
    
    def create_cart(self,customer):
        pass

    def add_to_cart(self,cart,product):
        pass

    def sale_confirm(self,cart):
        pass


