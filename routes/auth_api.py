from typing import Tuple, Any, Dict
from flask import Blueprint, jsonify, request
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)

from controller.auth import AuthenticationHandler


class AuthHandlerAPI:
    def __init__(self) -> None:
        """
        Initialize AuthHandlerAPI class.
        """
        self.ah = AuthenticationHandler()
        self.auth_api = Blueprint('auth_api', __name__)

    def register_routes(self) -> None:
        """
        Register routes for the AuthHandlerAPI class.
        """
        self.auth_api.route('/auth', methods=["POST"])(self.auth)

    def auth(self) -> Tuple[Dict[str, Any], int]:
        """
        Endpoint to handle user authentication.

        :return: JSON response containing the authentication token.
        :raises Exception: If there's an error verifying the Firebase ID token or authenticating the user with error code 400.
        """
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        if 'idToken' in request.json:
            id_token = request.json.get('idToken')
            try:
                return  self.ah.firebase_auth_test(id_token)
            except Exception as e:
                return jsonify({"msg":f"Error verifying Firebase ID token: {str(e)}"}), 400
        else:
            try:
                return  self.ah.authenticate(request.json.get("user"), request.json.get("password"))
            except Exception as e:
                return jsonify({"msg":f"Error authenticating user: {str(e)}"}), 400