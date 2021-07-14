import uuid
class sale:
    _id=""
    customer_id=""
    discount=0
    tax=0
    delivery_charge=0
    is_paid=False

    def __init__(self):
        self._id = str(uuid.uuid4())
        
    @classmethod
    def from_dict(self,dic):
        self._id=dic["_id"]
        self.customer_id=dic["customer_id"]
        self.discount=dic["discount"]
        self.tax=dic["tax"]
        self.delivery_charge=dic["delivery_charge"]
        self.is_paid=dic["is_paid"]