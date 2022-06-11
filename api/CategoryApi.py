from helper.CommonHelper import CommonHelper
from flask_restful import Resource, reqparse
from model.Category import Category
from service.CategoryService import CategoryService

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

delete_parser = reqparse.RequestParser()
delete_parser.add_argument('_id', type=str, required=True)


class CategoryApi(Resource):

    def __init__(self) -> None:
        super().__init__()
        self.service = CategoryService()

    def get(self):
        args = get_parser.parse_args()
        level = args['level']
        parent_id = args['parent_id']
        if not level:
            list_of_categories = self.service.get_categories(0, None)
        else:
            list_of_categories = self.service.get_categories(level, parent_id)
        return CommonHelper.objlist_to_dict(list_of_categories)

    def put(self):
        args = put_parser.parse_args()
        product = Category().from_dict(args)
        if not self.service.add_category(product):
            return "Invalid Data", 400
        return product.__dict__

    def delete(self):
        args = delete_parser.parse_args()
        product = Category().from_dict(args)
        if not self.service.delete_category(product):
            return "Invalid Data", 400
        self.service.delete_product(product)
        return "Success", 200
