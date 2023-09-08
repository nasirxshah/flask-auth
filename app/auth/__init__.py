from flask import Blueprint
from flask_restful import Api

from app.auth.resources import UserLogin, UserRegistration

auth_blueprint = Blueprint('Auth', __name__)
api = Api(auth_blueprint)

api.add_resource(UserRegistration, '/api/auth/signup')
api.add_resource(UserLogin, '/api/auth/signin')
