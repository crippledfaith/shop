from model.BaseModel import BaseModel


class Customer(BaseModel):

    
    def __init__(self):
        super().__init__()
        self.name = ""
        self.email = ""
        self.password = ""
