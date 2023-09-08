from datetime import timedelta

from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource

from app.auth.models import User


class UserRegistration(Resource):
    def post(self):
        user = User(**request.get_json())
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 201


class UserLogin(Resource):
    def post(self):
        body = request.get_json()
        print(body)
        user = User.objects.get(email=body['email'])
        if not user.check_password(body['password']):
            return "email and password did not match"

        expires = timedelta(hours=1)
        access_token = create_access_token(
            identity=str(user.id), expires_delta=expires)
        refresh_token = create_refresh_token(
            identity=str(user.id), expires_delta=expires)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
