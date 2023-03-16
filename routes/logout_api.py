from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)

from controller.auth import revoke_authentication


logout_api = Blueprint('logout_api', __name__)

# @logout_api.route("/logout", methods=["GET"])
# @jwt_required()
# def logout():
#     # jti = get_jwt()["jti"]
#     # print("11111",jti)
    
#     # redis_client.set(jti, "", ex=app.config["JWT_ACCESS_TOKEN_EXPIRES"])
#     return logout()


@logout_api.route("/logout", methods=["DELETE"])
@jwt_required()
def logout():
    """
    Logout user by revoking authentication token.

    :return: JSON response indicating successful logout.
    """

    try:
        # Get user identity from JWT token
        user = get_jwt_identity()

        # Revoke authentication token
        revoke_authentication(user)

        return jsonify({"msg": "Logout successful"}), 200

    except Exception as e:
        # Log error and return error message
        return jsonify({"msg": "Internal server error"}), 500
