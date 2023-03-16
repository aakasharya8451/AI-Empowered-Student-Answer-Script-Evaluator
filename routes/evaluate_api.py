from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask import Blueprint, request, jsonify
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)

from controller.evaluate import startEvaluate

evaluate_api = Blueprint('evaluate_api', __name__)


@evaluate_api.route('/evaluate', methods=["GET"])
@jwt_required()
def evaluate():
    """Evaluate the performance of the authenticated user.

    :return: JSON response or Tuple of JSON response and integer status code
    """

    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    if 'testid' not in request.json:
        return jsonify({"msg": "Missing testid parameter"}), 400
    else:
        testid = request.json.get('testid')
        try:
            return startEvaluate(testid)
        except Exception as e:
            return jsonify({"msg": "Internal server error"}), 500
            
