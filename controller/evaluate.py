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
    answer_set = fetch_query.fetchTests()
    question_set = fetch_query.fetchQuestions()
    # print(question_set)
    # print(answer_set)
    request = {}
    request["question_set"] = question_set
    request["answer_set"] = answer_set
    print(request)
    allotted_marks = Evaluator(request).evaluate()
    print(allotted_marks)
    fetch_query.pushMarks(allotted_marks)
    return jsonify({
        "testid": testid,
        'Evaluation': "Completed"}), 200
