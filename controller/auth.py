from flask import jsonify
from typing import Tuple, Dict, Any
from flask_jwt_extended import create_access_token, get_jwt
from firebase_admin import auth
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)

from config.config import Config
from utils.jwt_utils import redis_client


class AuthenticationHandler:
    def __init__(self) -> None:
        """
        Initialize AuthenticationHandler with Redis client.
        """
        self.redis_client = redis_client

    def revoke_authentication(self, user: str) -> Tuple[Dict[str, Any], int]:
        """
        Revoke authentication for the given user.

        :param user: str, username
        :return: Tuple of JSON response and integer status code
        """
        print(Config.JWT_ACCESS_TOKEN_EXPIRES)
        jti = get_jwt()["jti"]
        self.redis_client.set(jti, "", ex=Config.JWT_ACCESS_TOKEN_EXPIRES)
        return jsonify({"msg": "Successfully logged out", "user": user}), 200

    def authenticate(self, user: str, passwd: str) -> Tuple[Dict[str, Any], int]:
        """
        Authenticate user using username and password.

        :param user: str, username
        :param passwd: str, password
        :return: Tuple of JSON response and integer status code
        """
        if (user == "user" and passwd == "passwd") or (user == "test" and passwd == "test"):
            access_token = create_access_token(identity=user)
            return jsonify({
                "access": access_token,
                'user': user,
                'auth': "Success"}), 200
        else:
            return jsonify({"msg": "Bad username or password"}), 401

    def firebase_auth_test(self, id_token: str) -> Tuple[Dict[str, Any], int]:
        """
        Authenticate user using Firebase ID token.

        :param id_token: str, Firebase ID token
        :return: Tuple of JSON response and integer status code
        """
        try:
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token['uid']
            access_token = create_access_token(identity=uid)

            return jsonify({"access_token": access_token,
                            "user": uid,
                            "msg": "Authentication Successful"}), 200

        except Exception as e:
            print(e)
            return jsonify({f'error': f'Failed to authenticate - {e}'}), 401