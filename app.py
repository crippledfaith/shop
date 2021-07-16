from flask import Flask
from flask_restful import Api
from helper.RouteHelper import RouteHelper

app = Flask(__name__)
api = Api(app)
route_helper = RouteHelper(api)
route_helper.register_apis()

if __name__ == "__main__":
    app.run(debug=True)
