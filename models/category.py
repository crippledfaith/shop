import uuid
class category:
    _id=""
    name=""
    level=0
    parent_id=""
    
    def __init__(self,dic):
        self._id=dic["_id"]
        self.parent_id=dic["parent_id"]
        self.name=dic["name"]
        self.level=dic["level"]
        
    def __init__(self):
        self._id = str(uuid.uuid4())
    

