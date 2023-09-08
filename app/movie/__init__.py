from flask import Blueprint
from flask_restful import Api

from app.movie.resources import MovieDetail, MovieList

movie_blueprint = Blueprint('Movie', __name__)

api = Api(movie_blueprint)

api.add_resource(MovieList, '/api/movies')
api.add_resource(MovieDetail, '/api/movies/<string:id>')
