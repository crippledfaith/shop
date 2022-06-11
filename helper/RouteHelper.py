from flask_restful import Api
from api.CategoryApi import CategoryApi
from api.ProductApi import ProductApi

class RouteHelper:
    

    def __init__(self,api:Api) -> None:
        self.api = api
    
    def register_apis(self):
        self.api.add_resource(CategoryApi,"/catagory")
        self.api.add_resource(ProductApi,"/product")
