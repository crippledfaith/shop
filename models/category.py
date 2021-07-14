import uuid
class category:
    _id=""
    name=""
    level=0
    parent_id=""

    @classmethod
    def from_dict(self,dic):
        self._id=dic["_id"]
        self.parent_id=dic["parent_id"]
        self.name=dic["name"]
        self.level=dic["level"]
        return self

    def __init__(self):
        self._id = str(uuid.uuid4())
    

