import uuid


class Customer:
    
    def __init__(self):
        self._id = str(uuid.uuid4())
        self.name = ""
        self.email = ""
        self.password = ""

    @classmethod
    def from_dict(cls, dic):
        cls._id = dic["_id"]
        cls.name = dic["name"]
        cls.email = dic["email"]
        cls.password = dic["password"]
        return cls
