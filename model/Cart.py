import uuid


class Cart:
    
    def __init__(self):
        self._id = str(uuid.uuid4())
        self.sale_id = ""

    @classmethod
    def from_dict(cls, dic):
        cls._id = dic["_id"]
        cls.sale_id = dic["sale_id"]

