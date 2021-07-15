import uuid
from datetime import datetime

class BaseModel:

    def __init__(self) -> None:
        self._id = str(uuid.uuid4())
        self.creation_date = datetime.now()

    @classmethod
    def from_dict(cls, dic):
        
        for name_value in dic.keys():
            setattr(cls, name_value, dic[name_value])
        return cls