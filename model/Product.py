from model.BaseModel import BaseModel



class Product(BaseModel):

    def __init__(self):
        super().__init__()
        self.category_id = ""
        self.name = ""
        self.unit = ""
        self.mrp = 0
        self.price = 0
        self.tag = []

