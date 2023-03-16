# from controller.auth import firebase_auth_test
from flask import Blueprint, jsonify, request
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)

from controller.auth import authenticate, firebase_auth_test


auth_api = Blueprint('auth_api', __name__)


@auth_api.route('/auth', methods=["POST"])
def auth():
    """
    Endpoint to handle user authentication.

    :return: JSON response containing the authentication token.
    :raises Exception: If there's an error verifying the Firebase ID token or authenticating the user wih error code 400.
    """
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    if 'idToken' in request.json:
        id_token = request.json.get('idToken')
        try:
            return firebase_auth_test(id_token)
        except Exception as e:
            return jsonify({"msg":f"Error verifying Firebase ID token: {str(e)}"}), 400
    else:
        try:
            return authenticate(request.json.get("user"), request.json.get("password"))
        except Exception as e:
            return jsonify({"msg":f"Error authenticating user: {str(e)}"}), 400



# @auth_api.route('/auth', methods=["POST"])
# def auth():
    
#     if not request.is_json:
#         return jsonify({"msg": "Missing JSON in request"}), 400

#     # username = request.json.get("user", None)
#     # password = request.json.get("password", None)

#     # if not username:
#     #     return jsonify({"msg": "Missing username parameter"}), 400
#     # if not password:
#     #     return jsonify({"msg": "Missing password parameter"}), 400

#     # return authenticate(username, password)
#     id_token = request.json.get('idToken')
#     return firebase_auth_test(id_token)


    # if 'idToken' in request.json:
    #     id_token = request.json.get('idToken')
    #     try:
    #         return firebase_auth_test(id_token)
    #     except Exception as e:
    #         return jsonify({"msg": "Error verifying Firebase ID token"}), 400
    # else:
    #     try:
    #         return authenticate(request.json)
    #     except Exception as e:
    #         return Exception({"msg": "Error authenticating user"}), 400
    # # else:
    # #     return jsonify({"msg": "Missing username id_token"}), 400
