import mongoengine

class Database():
    def init_app(self,app):
        mongoengine.connect(host=app.config["MONGO_URI"])


db = Database()