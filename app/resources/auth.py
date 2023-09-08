from flask_restful import Resource
from flask import request
from app.database.models import User
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

class UserRegistration(Resource):
    def post(self):
        user  = User(**request.get_json())
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 201


class UserLogin(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body['email'])
        if not user.check_password(body['password']):
            return "email and password did not match"
        
        expires = timedelta(hours=1)
        access_token = create_access_token(identity=str(user.id),expires_delta=expires)
        refresh_token = create_refresh_token(identity=str(user.id),expires_delta=expires)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }