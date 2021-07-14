import uuid


class Tag:
    _id = ""
    name = ""

    def __init__(self):
        self._id = str(uuid.uuid4())

    @classmethod
    def from_dict(cls, dic):
        cls._id = dic["_id"]
        cls.name = dic["name"]
