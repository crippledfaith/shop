from model.BaseModel import BaseModel


class SaleItem(BaseModel):

    def __init__(self):
        super().__init__()
        self.sale_id = ""
        self.item_id = ""
        self.price = 0
        self.quantity = 0
        self.discount = 0
