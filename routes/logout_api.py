from flask import Blueprint, jsonify
from typing import Tuple, Any, Dict
from flask_jwt_extended import jwt_required, get_jwt_identity
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)

from controller.auth import AuthenticationHandler


class LogoutAPI:
    def __init__(self) -> None:
        """
        Initialize LogoutAPI class.
        """
        self.logout_api = Blueprint('logout_api', __name__)
        self.ah = AuthenticationHandler()

    def register_routes(self) -> None:
        """
        Register routes for the LogoutAPI class.
        """
        self.logout_api.route("/logout", methods=["DELETE"])(self.logout)

    @jwt_required()
    def logout(self) -> Tuple[Dict[str, Any], int]:
        """
        Logout user by revoking authentication token.

        :return: JSON response indicating successful logout.
        """
        try:
            user = get_jwt_identity()
            self.ah.revoke_authentication(user)
            return jsonify({"msg": "Logout successful"}), 200

        except Exception as e:
            return jsonify({"msg": f"Internal server error {e}"}), 500