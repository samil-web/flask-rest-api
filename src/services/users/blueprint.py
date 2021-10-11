from flask import Blueprint

from flask_restful import Api

from controller import UsersHandler,UserHandler

"""

Blueprint is about you are letting know flask application that you  have users endpoint

"""


users = Blueprint('users', __name__)#

api = Api(users)#initializes the fact that we use restful api

api.add_resource(UsersHandler, '/users')

api.add_resource(UserHandler, '/users/<string:id>')

# if __name__ == '__main__':
#     users.run(debug = True)

 

