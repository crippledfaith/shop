import uuid
from datetime import datetime


class BaseModel:

    def __init__(self) -> None:
        self._id = str(uuid.uuid4())

    def from_dict(self, dic):
        for name_value in dic.keys():
            setattr(self, name_value, dic[name_value])
        return self