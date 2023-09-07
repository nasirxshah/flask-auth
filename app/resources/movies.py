from flask_restful import Resource
from app.database.models import Movie
from flask import request, Response

class MoviesApi(Resource):
  def get(self):
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)

  def post(self):
    body = request.get_json()
    movie = Movie(**body).save()
    id = movie.id
    return {'id': str(id)}, 200
 
class MovieApi(Resource):
  def put(self, id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return '', 200
 
  def delete(self, id):
    movie = Movie.objects.get(id=id).delete()
    return '', 200

  def get(self, id):
    movies = Movie.objects.get(id=id).to_json()
    return Response(movies, mimetype="application/json", status=200)


movies = [
    {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    {
       "name": "The Godfather ",
       "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
       "genres": ["Crime", "Drama"]
    }
]