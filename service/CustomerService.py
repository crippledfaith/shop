from db_context.QueryContext import QueryContext
from model.Customer import Customer


class CustomerService:
    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
            cls.__instance.context = QueryContext()
        return cls.__instance

    def add_customer(self, obj):
        email_exits = self.context.get_all_by_condition(
            "customer", {"email": obj.email}).count()
        if email_exits > 0:
            return False
        self.context.save('customer', obj.__dict__)
        return True

    def update_customer(self, obj):
        if obj._id != "":  # will not allow if there is no object id
            main_customer = self.get_customer(obj._id)
            if main_customer is None:
                return False
        else:
            return False
        email_exits = self.context.get_all_by_condition(
            "customer", {"email": obj.email}).count()
        if main_customer.email != obj.email and email_exits > 0:
            return False
        self.context.update('customer', obj.__dict__)

    def delete_customer(self, obj):
        if obj._id != "":
            main_customer = self.get_customer(obj._id)
            if main_customer is None:
                return False
        else:
            return False
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
