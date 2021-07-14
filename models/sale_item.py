import uuid
class sale_item:
    _id=""
    saleid=""
    itemid=""
    price=0
    quantity=0
    discount=0

    def __init__(self):
        self._id = str(uuid.uuid4())

    def __init__(self,dic):
        self._id=dic["_id"]
        self.saleid=dic["saleid"]
        self.itemid=dic["itemid"]
        self.quantity=dic["quantity"]
        self.discount=dic["discount"]
