import uuid


class Sale:


    def __init__(self):
        self._id = str(uuid.uuid4())
        self.customer_id = ""
        self.discount = 0
        self.tax = 0
        self.delivery_charge = 0
        self.is_paid = False

    @classmethod
    def from_dict(cls, dic):
        cls._id = dic["_id"]
        cls.customer_id = dic["customer_id"]
        cls.discount = dic["discount"]
        cls.tax = dic["tax"]
        cls.delivery_charge = dic["delivery_charge"]
        cls.is_paid = dic["is_paid"]
        return cls
