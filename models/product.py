from models.category import category
import uuid
class product:
    _id=""
    categoryid=""
    name=""
    unit=""
    mrp=0
    price=0
    tag=[]

    def __init__(self):
        self._id = str(uuid.uuid4())
    
    def __init__(self,dic):
        self._id=dic["_id"]
        self.categoryid=dic["categoryid"]
        self.name=dic["name"]
        self.unit=dic["unit"]
        self.mrp=dic["mrp"]
        self.price=dic["price"]
        self.tag=dic["tag"]
