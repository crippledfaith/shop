from helper.CommonHelper import CommonHelper
from model.Product import Product
from flask_restful import Resource, reqparse
from service.ProductService import ProductService
import json

get_parser = reqparse.RequestParser()
get_parser.add_argument('level', type=int, required=False)
get_parser.add_argument('parent_id', type=str, required=False)

put_parser = reqparse.RequestParser()
put_parser.add_argument('name', type=str, required=True,
                        help="name is required")
put_parser.add_argument('level', type=int, required=True,
                        help="level is required")
put_parser.add_argument('parent_id', type=str,
                        required=True, help="parent_id is required")


class CatagoryApi(Resource):

    def __init__(self) -> None:
        super().__init__()
        self.service = ProductService()

    def get(self):
        args = get_parser.parse_args()
        level = args['level']
        parent_id = args['parent_id']
        if(not level):
            list_of_categories = self.service.get_categories(0, None)
        else:
            list_of_categories = self.service.get_categories(level, parent_id)
        return CommonHelper().objlist_to_dict(list_of_categories)

    def put(self):
        args = put_parser.parse_args()
        product = Category().from_dict(args)
        self.service.add_category(product)
        return product.__dict__