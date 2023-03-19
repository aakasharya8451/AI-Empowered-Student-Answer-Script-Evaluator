from typing import Dict
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)

# from config.config_firebase import FirebaseHandler
from utils.custom_errors import FirebaseQuerryError
from config.config_firebase import db


class FirebaseQuery:
    def __init__(self, testid: str) -> None:
        """
        Create a new FirebaseQuery instance to fetch test and question data from Firebase

        :param testid: The ID of the test to fetch data for
        :type testid: str
        """
        self.testid = testid
        # self.firebase_handler = FirebaseHandler()

    def fetchTests(self) -> Dict[str, Dict[str, str]]:
        """
        Fetches test data for the current test ID

        :return: A dictionary containing test data
        :rtype: Dict[str, Dict[str, str]]
        :raises FirebaseQuerryError: If there is an error fetching test data from Firebase
        """
        try:
            student_collections_ref = db.collection(
                u'tests').document(u'{}'.format(self.testid))
            student_collections = student_collections_ref.collections()

            test_answer_set = {}
            for student in student_collections:
                answer = {}
                for question in student.stream():
                    answer[question.id] = question.to_dict()['ans']
                test_answer_set[student.id] = answer
            return test_answer_set

        except Exception as e:
            raise FirebaseQuerryError(f"Error fetching test data: {e}")

    def fetchQuestions(self) -> Dict[str, Dict[str, str]]:
        """
        Fetches question data for the current test ID

        :return: A dictionary containing question data
        :rtype: Dict[str, Dict[str, str]]
        :raises FirebaseQuerryError: If there is an error fetching question data from Firebase
        """
        try:
            test_question_set = db.collection(
                u'questionset').document(u'{}'.format(self.testid)).get().to_dict()
            return test_question_set

        except Exception as e:
            raise FirebaseQuerryError(
                f"Error fetching question data: {e}")
    
    def pushMarks(self,assigned_marks):
        """Updates the 'marks' field for all questions in the test that were attempted by students.

        :param assigned_marks: a dictionary where the keys are student IDs and the values are dictionaries that map
                               question IDs to their assigned marks.
        :return: True if all updates were successful, False otherwise.
        :raises FirebaseQuerryError: if there was an error updating the marks.
        """
        try:
            student_collections_ref = db.collection(
                u'tests').document(u'{}'.format(self.testid))
            student_collections = student_collections_ref.collections()
            test_detail_doc = db.collection(u'testDetails').document(u'{}'.format(self.testid))
            for student in student_collections:
                for question in student.stream():
                    path = u"tests/{}/{}/{}".format(self.testid,
                                                    student.id, question.id)
                    marks = assigned_marks.get(student.id, "").get(question.id)
                    doc_ref = db.document(path)
                    doc_ref.update({u'marks': marks})
            test_detail_doc.update({u'evaluationStatus' : True})
            return True
        except Exception as e:
            raise FirebaseQuerryError(
                f"Error fetching question data: {e}")


if __name__ == "__main__":
    let_marks = {'NC4xNH3w8IZ9twWwLycZKq9wxz93': {'q1': 9.5, 'q2': 2.0},
               'SZUBmedhAOSCpSlfUovNINTQ8fr1': {'q1': 10.0, 'q2': 1.5}}
    z = FirebaseQuery("PczMwm2P78Hi85gQzER8")

    print(z.fetchTests())
    print(z.fetchQuestions())
    print(z.pushMarks(let_marks))

