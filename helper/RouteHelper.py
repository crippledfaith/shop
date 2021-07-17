from flask_restful import Api
from api.CatagoryApi import CatagoryApi
from api.ProductApi import ProductApi

class RouteHelper:
    

    def __init__(self,api:Api) -> None:
        self.api = api
    
    def register_apis(self):
        self.api.add_resource(CatagoryApi,"/catagory")
        self.api.add_resource(ProductApi,"/product")
