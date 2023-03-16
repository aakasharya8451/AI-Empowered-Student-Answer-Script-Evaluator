from flask import jsonify
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)

from models.firebase_query import FirebaseQuery
from evaluation_engine.evaluator import Evaluator


def startEvaluate(testid):
    fetch_query = FirebaseQuery(testid)
    question_set = fetch_query.fetchTests()
    answer_set = fetch_query.fetchQuestions()
    print(question_set)
    print(answer_set)
    request = {}
    request["question_set"] = question_set
    request["answer_set"] = answer_set
    allotted_marks = Evaluator(request).evaluate()
    fetch_query.pushMarks(allotted_marks)
    return jsonify({
        "user": testid,
        'Evaluation': "Started"}), 200
