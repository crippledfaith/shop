import uuid


class SaleItem:
    _id = ""
    sale_id = ""
    item_id = ""
    price = 0
    quantity = 0
    discount = 0

    def __init__(self):
        self._id = str(uuid.uuid4())

    @classmethod
    def from_dict(cls, dic):
        cls._id = dic["_id"]
        cls.sale_id = dic["sale_id"]
        cls.item_id = dic["item_id"]
        cls.quantity = dic["quantity"]
        cls.discount = dic["discount"]
