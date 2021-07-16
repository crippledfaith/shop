from api.CatagoryApi import CatagoryApi
from flask_restful import Api

class RouteHelper:
    

    def __init__(self,api:Api) -> None:
        self.api = api
    
    def register_apis(self):
        self.api.add_resource(CatagoryApi,"/catagory")
