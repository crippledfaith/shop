import uuid
class customer:
    _id=""
    name=""

    def __init__(self):
        self._id = str(uuid.uuid4())
    
    def __init__(self,dic):
        self._id=dic["_id"]
        self.name=dic["name"]
