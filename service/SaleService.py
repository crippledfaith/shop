from model.Sale import Sale
from db_context.QueryContext import QueryContext


class SaleService:
    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
            cls.__instance.context = QueryContext()
        return cls.__instance

    def add_sale(self, obj):
        self.context.save('sale', obj.__dict__)

