from flask_restful import Api
from flask import Blueprint
from app.resources.movies import MoviesList

movies_bp = Blueprint("Movies",__name__)
api = Api(movies_bp)
api.add_resource(MoviesList, "/movies/")