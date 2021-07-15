from model.BaseModel import BaseModel


class Category(BaseModel):

    def __init__(self):
        super().__init__()
        self.name = ""
        self.level = 0
        self.parent_id = ""
        

   

