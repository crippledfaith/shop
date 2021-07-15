import uuid


class SaleItem:

    def __init__(self):
        self._id = str(uuid.uuid4())
        self.sale_id = ""
        self.item_id = ""
        self.price = 0
        self.quantity = 0
        self.discount = 0

    @classmethod
    def from_dict(cls, dic):
        cls._id = dic["_id"]
        cls.sale_id = dic["sale_id"]
        cls.item_id = dic["item_id"]
        cls.quantity = dic["quantity"]
        cls.discount = dic["discount"]
        return cls
