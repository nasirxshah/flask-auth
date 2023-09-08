from flask import Flask
from app.resources.routes import movies_bp
from app.database.db import db 
from app.extensions import bcrypt, jwt
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)


    app.register_blueprint(movies_bp)

    return app