import mongoengine
from flask import Flask

from app.auth import auth_blueprint
from app.extensions import bcrypt, jwt
from app.movie import movie_blueprint
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    mongoengine.connect(host=app.config["MONGO_URI"])

    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(movie_blueprint)

    return app
