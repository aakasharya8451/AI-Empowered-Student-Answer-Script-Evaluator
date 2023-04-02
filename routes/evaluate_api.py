from flask_jwt_extended import jwt_required
from flask import Blueprint, request, jsonify
from typing import Tuple, Any, Dict
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)

from controller.evaluate import EvaluationHandler

class EvaluateAPI:
    def __init__(self):
        """
        Initialize EvaluateAPI class.
        """
        self.evaluate_api = Blueprint('evaluate_api', __name__)

    def register_routes(self):
        """
        Register routes for the EvaluateAPI class.
        """
        self.evaluate_api.add_url_rule('/evaluate', methods=["POST"], view_func=self.evaluate)

    @jwt_required()
    def evaluate(self) -> Tuple[Dict[str, Any], int]:
        """
        Initiate performance evaluation for the assigned test by the authenticated user, using the corresponding test ID.

        :param testid: str, test id parameter
        :return: Tuple of JSON response and integer status code
        """
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        if 'testid' not in request.json:
            return jsonify({"msg": "Missing testid parameter"}), 400

        testid = request.json.get('testid')
        try:
            self.eh = EvaluationHandler(testid)
            return self.eh.start_evaluation()
        except Exception as e:
            return jsonify({"msg": f"Internal server error {e}"}), 500
        
# EvaluationHandler("PczMwm2P78Hi85gQzER8").start_evaluation()