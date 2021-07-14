import uuid
class category:
    _id=""
    categoryid=""
    name=""
    level=0

    def __init__(self):
        self._id = str(uuid.uuid4())
    
    def __init__(self,dic):
        self._id=dic["_id"]
        self.categoryid=dic["categoryid"]
        self.name=dic["name"]
        self.level=dic["level"]
