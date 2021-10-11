from flask import Blueprint

from flask_restful import Api

from src.services.users.controller import UsersHandler,UserHandler

"""

Blueprint is about you are letting know flask application that you  have users endpoint

"""


users = Blueprint('users', __name__)

api = Api(users)

api.add_resource(UsersHandler, '/users')

api.add_resource(UserHandler, '/users/<string:id>')


 

