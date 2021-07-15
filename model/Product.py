import uuid


class Product:
    _id = ""


    def __init__(self):
        self._id = str(uuid.uuid4())
        self.category_id = ""
        self.name = ""
        self.unit = ""
        self.mrp = 0
        self.price = 0
        self.tag = []

    @classmethod
    def from_dict(cls, dic):
        cls._id = dic["_id"]
        cls.category_id = dic["category_id"]
        cls.name = dic["name"]
        cls.unit = dic["unit"]
        cls.mrp = dic["mrp"]
        cls.price = dic["price"]
        cls.tag = dic["tag"]
        return cls
