import uuid
class cart:
    _id=""
    sale_id=""

    def __init__(self):
        self._id = str(uuid.uuid4())

    def __init__(self,dic):
        self._id=dic["_id"]
        self.sale_id=dic["sale_id"]
