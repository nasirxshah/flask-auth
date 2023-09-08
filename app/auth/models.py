import mongoengine as mongo
from flask_bcrypt import check_password_hash, generate_password_hash


class User(mongo.Document):
    email = mongo.EmailField(required=True, unique=True)
    password = mongo.StringField(required=True)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
