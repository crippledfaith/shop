import uuid


class Cart:
    _id = ""
    sale_id = ""

    def __init__(self):
        self._id = str(uuid.uuid4())

    @classmethod
    def from_dict(cls, dic):
        cls._id = dic["_id"]
        cls.sale_id = dic["sale_id"]
