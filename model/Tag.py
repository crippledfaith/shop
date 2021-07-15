import uuid


class Tag:

    def __init__(self):
        self._id = str(uuid.uuid4())
        self.name = ""

    @classmethod
    def from_dict(cls, dic):
        cls._id = dic["_id"]
        cls.name = dic["name"]
        return cls
