from model.BaseModel import BaseModel


class Sale(BaseModel):

    def __init__(self):
        super().__init__()
        self.customer_id = ""
        self.discount = 0
        self.tax = 0
        self.delivery_charge = 0
        self.is_paid = False

