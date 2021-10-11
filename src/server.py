from flask import Flask

from src.services.users.blueprint import users as users_blueprint

from src.error_handler import handle_bad_request 

from dotenv import load_dotenv

load_dotenv()

application = Flask(__name__)

application.register_blueprint(users_blueprint)

application.register_error_handler(400, handle_bad_request)

