import uuid
class customer:
    _id=""
    name=""
    email=""
    password=""

    def __init__(self):
        self._id = str(uuid.uuid4())
        
    @classmethod
    def from_dict(self,dic):
        self._id=dic["_id"]
        self.name=dic["name"]
        self.email=dic["email"]
        self.password=dic["password"]