from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Category import CategoryResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# routes
api.add_resource(Hello, '/hello')
api.add_resource(CategoryResource, '/category')
