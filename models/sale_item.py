import uuid
class sale_item:
    _id=""
    sale_id=""
    item_id=""
    price=0
    quantity=0
    discount=0

    def __init__(self):
        self._id = str(uuid.uuid4())

    def __init__(self,dic):
        self._id=dic["_id"]
        self.sale_id=dic["sale_id"]
        self.item_id=dic["item_id"]
        self.quantity=dic["quantity"]
        self.discount=dic["discount"]
