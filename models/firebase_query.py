from typing import Dict
from firebase_admin import firestore
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)

from utils.custom_errors import FirebaseQueryError


class FirebaseQuery:
    def __init__(self, test_id: str) -> None:
        """
        Create a new FirebaseQuery instance to fetch test and question data from Firebase

        :param testid: The ID of the test to fetch data for
        :type testid: str
        """
        self.test_id = test_id
        self.db = firestore.client()

    def fetch_tests(self) -> Dict[str, Dict[str, str]]:
        """
        Fetches test data for the current test ID

        :return: A dictionary containing test data
        :rtype: Dict[str, Dict[str, str]]
        :raises FirebaseQuerryError: If there is an error fetching test data from Firebase
        """
        try:
            student_collections_ref = self.db.collection(
                u'tests').document(self.test_id)
            student_collections = student_collections_ref.collections()

            test_answer_set = {}
            for student in student_collections:
                answer = {}
                for question in student.stream():
                    answer[question.id] = question.to_dict()['ans']
                test_answer_set[student.id] = answer
            return test_answer_set

        except Exception as e:
            raise FirebaseQueryError(f"Error fetching test data: {e}")

    def fetch_questions(self) -> Dict[str, Dict[str, str]]:
        """
        Fetches question data for the current test ID

        :return: A dictionary containing question data
        :rtype: Dict[str, Dict[str, str]]
        :raises FirebaseQuerryError: If there is an error fetching question data from Firebase
        """
    def fetch_questions(self) -> Dict[str, Dict[str, str]]:
        """
        Fetches question data for the current test ID

        :return: A dictionary containing question data
        :rtype: Dict[str, Dict[str, str]]
        :raises FirebaseQueryError: If there is an error fetching question data from Firebase
        """
        try:
            test_question_set = self.db.collection(u'questionset').document(self.test_id).get().to_dict()
            return test_question_set
        except Exception as e:
            raise FirebaseQueryError(f"Error fetching question data: {e}")
    
    def push_marks(self,assigned_marks):
        """Updates the 'marks' field for all questions in the test that were attempted by students.

        :param assigned_marks: a dictionary where the keys are student IDs and the values are dictionaries that map
                               question IDs to their assigned marks.
        :return: True if all updates were successful, False otherwise.
        :raises FirebaseQuerryError: if there was an error updating the marks.
        """
        try:
            students_collection_ref = self.db.collection(
                u'tests').document(self.test_id).collections()
            test_detail_doc = self.db.collection(u'testDetails').document(self.test_id)

            for student in students_collection_ref:
                for question in student.stream():
                    path = f"tests/{self.test_id}/{student.id}/{question.id}"
                    marks = assigned_marks.get(student.id, {}).get(question.id)
                    doc_ref = self.db.document(path)
                    doc_ref.update({u'marks': marks})

            test_detail_doc.update({u'evaluationStatus': True})
            return True
        except Exception as e:
            raise FirebaseQueryError(f"Error pushing marks: {e}")