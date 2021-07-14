import uuid
class cart:
    _id=""
    customerid=""
    saleid=[]

    def __init__(self):
        self._id = str(uuid.uuid4())

    def __init__(self,dic):
        self._id=dic["_id"]
        self.customerid=dic["customerid"]
        self.saleid=dic["saleid"]
