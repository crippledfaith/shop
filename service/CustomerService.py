from db_context.QueryContext import QueryContext


class CustomerService():

    __instance = None
    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
            cls.__instance.context = QueryContext()
        return cls.__instance
        


    def add_customer(self):
        return

    def update_customer(self):
        return

    def delete_customer(self):
        return
