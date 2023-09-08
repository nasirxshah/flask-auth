from flask_restful import Api
from flask import Blueprint
from app.resources.movies import MovieList, MovieDetail
from app.resources.auth import UserRegistration, UserLogin

movies_bp = Blueprint("Movies",__name__)
api = Api(movies_bp)


api.add_resource(MovieList, "/movies/")
api.add_resource(MovieDetail,"/movies/<string:id>")
api.add_resource(UserRegistration,"/api/auth/signup")
api.add_resource(UserLogin,"/api/auth/login")