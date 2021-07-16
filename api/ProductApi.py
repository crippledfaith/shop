from flask_restful import Resource,reqparse

get_parser = reqparse.RequestParser()
get_parser.add_argument('id', type=int, required=False)
get_parser.add_argument('analysis', type=bool, default=False, required=False, help='Enable analysis')

class ProductApi(Resource):
    def get(self):
        args = get_parser.parse_args()
        classes = args['id']  # List ['A', 'B']
        analysis = args['analysis'] # Boolean True
        return {"name":"test"}
