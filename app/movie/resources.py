from flask import Response, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.movie.models import Movie


class MovieList(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        body = request.get_json()
        movie = Movie(**body).save()
        id = movie.id
        return {'id': str(id)}, 200


class MovieDetail(Resource):
    @jwt_required()
    def put(self, id):
        body = request.get_json()
        Movie.objects.get(id=id).update(**body)
        return '', 200

    @jwt_required()
    def delete(self, id):
        movie = Movie.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        movies = Movie.objects.get(id=id).to_json()
        return Response(movies, mimetype="application/json", status=200)
