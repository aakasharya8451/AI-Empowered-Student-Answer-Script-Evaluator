from flask import jsonify
from typing import Tuple, Dict, Any
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)

from models.firebase_query import FirebaseQuery
from evaluation_engine.evaluator import Evaluator


class EvaluationHandler:
    def __init__(self, test_id: str) -> None:
        """
        Initializes the EvaluationHandler class with a test ID.

        :param test_id: str, test ID parameter
        """
        self.test_id = test_id
    
    def start_evaluation(self) -> Tuple[Dict[str, Any], int]:
        """
        Begins evaluating the assigned test's performance by the authenticated user, 
        based on the corresponding test ID.

        :return: Tuple of JSON response and integer status code
        """
        fetch_query = FirebaseQuery(self.test_id)
        answer_set = fetch_query.fetch_tests()
        question_set = fetch_query.fetch_questions()
        request = {"question_set": question_set, "answer_set": answer_set}
        allotted_marks = Evaluator(request).evaluate()
        fetch_query.push_marks(allotted_marks)
        return jsonify({
            "testid": self.test_id,
            "evaluation": "Completed"
        }), 200