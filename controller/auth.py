from flask import jsonify
from flask_jwt_extended import create_access_token, get_jwt
from firebase_admin import auth
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)

from config.config_redis import RedisHandler
from config.config import jwt, Config


redis_client = RedisHandler().get_redis_client()

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header,decrypted_token):
    jti = decrypted_token["jti"]
    token_in_blacklist = redis_client.get(jti)
    return token_in_blacklist is not None

def revoke_authentication(user):
    jti = get_jwt()["jti"]
    redis_client.set(jti, "", ex = Config.JWT_ACCESS_TOKEN_EXPIRES)
    return jsonify({"msg": "Successfully logged out", "user": user}), 200

def authenticate(user, passwd):
    """
    Authenticate user using username and password.

    :param user: str, username
    :param passwd: str, password
    :return: JSON response or Tuple of JSON response and integer status code
    """
    if (user == "user" and passwd == "passwd") or (user == "test" and passwd == "test"):
        access_token = create_access_token(identity=user)
        return jsonify({
            "access": access_token,
            'user': user,
            'auth': "Success"}), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401
    

def firebase_auth_test(id_token):
    """
    Authenticate user using Firebase ID token.

    :param id_token: str, Firebase ID token
    :return: JSON response or Tuple of JSON response and integer status code
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
