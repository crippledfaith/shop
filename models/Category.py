import uuid


class Category:
    _id = ""
    name = ""
    level = 0
    parent_id = ""

    @classmethod
    def from_dict(cls, dic):
        cls._id = dic["_id"]
        cls.parent_id = dic["parent_id"]
        cls.name = dic["name"]
        cls.level = dic["level"]
        return cls

    def __init__(self):
        self._id = str(uuid.uuid4())
