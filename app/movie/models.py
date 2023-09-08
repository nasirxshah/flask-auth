import mongoengine as mongo


class Movie(mongo.Document):
    name = mongo.StringField(required=True, unique=True)
    casts = mongo.ListField(mongo.StringField(), required=True)
    genres = mongo.ListField(mongo.StringField(), required=True)
