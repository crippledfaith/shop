import uuid


class Product:
    _id = ""
    category_id = ""
    name = ""
    unit = ""
    mrp = 0
    price = 0
    tag = []

    def __init__(self):
        self._id = str(uuid.uuid4())

    @classmethod
    def from_dict(cls, dic):
        cls._id = dic["_id"]
        cls.category_id = dic["category_id"]
        cls.name = dic["name"]
        cls.unit = dic["unit"]
        cls.mrp = dic["mrp"]
        cls.price = dic["price"]
        cls.tag = dic["tag"]
