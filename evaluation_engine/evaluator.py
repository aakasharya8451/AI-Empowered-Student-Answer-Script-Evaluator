import os
import sys

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)

from evaluation_engine.pattern_matching.fixed_pattern import FixedPatternMatching
from evaluation_engine.pattern_matching.partial_pattern import PartialPatternMatching
from evaluation_engine.marks_assigner.marks_assigner import MarksAssigner


class Evaluator:
    def __init__(self, requests: dict) -> None:
        """Constructor for Evaluator.

        :param requests: Dictionary containing data for evaluation purpose.
        :type requests: dict
        :raises ValueError: If answer_set or question_set keys are not found in requests dictionary.
        """

        if "answer_set" not in requests:
            raise ValueError(
                "answer_set key not found in requests dictionary.")
        if "question_set" not in requests:
            raise ValueError(
                "question_set key not found in requests dictionary.")

        self.requests = requests

    def evaluate(self) -> dict[list[float]]:
        """Function to calculate marks corresponding to answers and their keywords.

        :return: Dictionary containing marks for each question and answer for each student.
        :rtype: dict[list[float]]
        :raises ValueError: If the keywords or maximum marks are not found for a question.
        """

        response_marks = {}
        answer_set = self.requests.get("answer_set", {})
        question_set = self.requests.get("question_set", {})

        # Iterate over each student's answers
        for student_id, answers in answer_set.items():
            per_student_marks = {}

            # Iterate over each question's answer for the current student
            for question in answers:
                # Get answer for the current question
                answer = answers.get(question)
                # Get keywords and maximum marks for the current question
                keywords = question_set.get(question).get("keywords")
                max_marks = question_set.get(question).get("marks")

                # Check if keywords or maximum marks are None, raise ValueError if so
                if keywords is None:
                    raise ValueError(
                        f"Keywords not found for question {question}")

                if max_marks is None:
                    raise ValueError(
                        f"Maximum marks not found for question {question}")

                # If answer is empty string, assigning 0.0 marks
                if not answer.strip():
                    per_student_marks[question] = 0.0
                    continue

                try:
                    # Run fixed and partial pattern matching to calculate marks
                    fixed_pattern_matching = FixedPatternMatching(
                        keywords, answer).run()
                    partial_pattern_matching = PartialPatternMatching(
                        keywords, answer).run()
                    assign_marks = MarksAssigner(
                        fixed_pattern_matching, partial_pattern_matching, max_marks).assign()
                    per_student_marks[question] = (float(assign_marks))

                except Exception as e:
                    # If an error occurs while calculating marks, raise ValueError
                    raise ValueError(
                        f"Error occurred while evaluating answer '{answer}' of student {student_id} for question {question} keywords {keywords} and marks {max_marks}: {e}")

            # Store the calculated marks for the current student's answers
            response_marks[student_id] = per_student_marks

        return response_marks


if __name__ == "__main__":
    request_old = {
        "question_set": {
            "q1": {"keywords": ["Alan Turing", "alan"], "marks": 10},
            "q2": {"keywords": ["Charles Babbage", "Charles"], "marks": 2}
        },
        "answer_set": {
            "s1": {"q1": "The father alam of modern computer is Ala Turin Ala Turin Ala Turing",
                   "q2": "The father of computer is Charles Babbage"},
            "s2": {"q1": "",
                   "q2": ""}
        }
    }

    e = Evaluator(request_old).evaluate()
    print(request_old.get("answer_set"))
    print(e)
