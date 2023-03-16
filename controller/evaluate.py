from flask import jsonify
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)

from models.firebase_query import FirebaseQuery


def startEvaluate(testid):
    fetch_query = FirebaseQuery(testid)
    print(fetch_query.fetchTests())
    print(fetch_query.fetchQuestions())
    return jsonify({
        "user": testid,
        'Evaluation': "Started"}), 200
