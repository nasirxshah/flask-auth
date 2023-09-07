from flask import Flask
from app.resources.routes import movies_bp
from app.database.db import db 

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/movie"
    db.init_app(app)
    app.register_blueprint(movies_bp)

    return app