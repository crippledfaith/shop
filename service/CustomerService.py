from db_context.QueryContext import QueryContext
from model.Customer import Customer


class CustomerService():
    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
            cls.__instance.context = QueryContext()
        return cls.__instance
        
    def add_customer(self, obj):
        self.context.save('customer', obj.__dict__)

    def update_customer(self, obj):
        self.context.update('customer', obj.__dict__)

    def delete_customer(self, obj):
        self.context.delete('customer', obj.__dict__)
    
    def get_customers(self):
        customer_list = []
        customers = self.context.get_all('customer')
        for items in customers:
            customer_list.append(Customer().from_dict(items))
        return customer_list

    def get_customer(self, customer_id):
        customer = self.context.get_item_by_id('customer', customer_id)
        return Customer().from_dict(customer)
