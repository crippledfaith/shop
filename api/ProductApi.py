from helper.CommonHelper import CommonHelper
from model.Product import Product
from flask_restful import Resource, reqparse
from service.ProductService import ProductService

get_parser = reqparse.RequestParser()
get_parser.add_argument('product_id', type=str, required=False)
get_parser.add_argument('category_id', type=str, required=False)

put_parser = reqparse.RequestParser()
put_parser.add_argument('name', type=str, required=True,
                        help="name is required")
put_parser.add_argument('unit', type=str, required=True,
                        help="level is required")
put_parser.add_argument('category_id', type=str, 
                        required=True, 
                        help="category_id is required")
put_parser.add_argument('mrp', type=int,
                        required=True, 
                        help="mrp is required")
put_parser.add_argument('price', type=int,
                        required=True, 
                        help="price is required")
put_parser.add_argument('tag', type=list,
                        required=True, 
                        help="tag is required",location="json")

delete_parser = reqparse.RequestParser()
delete_parser.add_argument('_id', type=str, required=True)

class ProductApi(Resource):

    def __init__(self) -> None:
        super().__init__()
        self.service = ProductService()

    def get(self):
        args = get_parser.parse_args()
        product_id = args['product_id']
        category_id = args['category_id']
        if not product_id and not category_id:
            list_of_products = self.service.get_products(None)
        elif not product_id and category_id:
            list_of_products = self.service.get_products(category_id)
        elif product_id and not category_id:
            product = self.service.get_product(product_id)
            return product.__dict__
        return CommonHelper().objlist_to_dict(list_of_products)

    def put(self):
        args = put_parser.parse_args()
        product = Product().from_dict(args)
        self.service.add_product(product)
        return product.__dict__
    
    def delete(self):
        args = delete_parser.parse_args()
        product = Product().from_dict(args)
        self.service.delete_product(product)
        return
