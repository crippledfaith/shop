import uuid


class Sale:
    _id = ""
    customer_id = ""
    discount = 0
    tax = 0
    delivery_charge = 0
    is_paid = False

    def __init__(self):
        self._id = str(uuid.uuid4())

    @classmethod
    def from_dict(cls, dic):
        cls._id = dic["_id"]
        cls.customer_id = dic["customer_id"]
        cls.discount = dic["discount"]
        cls.tax = dic["tax"]
        cls.delivery_charge = dic["delivery_charge"]
        cls.is_paid = dic["is_paid"]
