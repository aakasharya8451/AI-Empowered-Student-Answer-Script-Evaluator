import unittest
from unittest.mock import Mock
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)
from evaluation_engine.evaluator import Evaluator


class TestEvaluator(unittest.TestCase):

    def setUp(self):
        self.answer_set = {
            "s1": {
                "q1": "This is a sample answer.",
                "q2": "Another sample answer.",
            },
            "s2": {
                "q1": "Sample answer for question 1.",
                "q2": "Yet another sample answer.",
            }
        }
        self.question_set = {
            "q1": {
                "keywords": ["sample", "answer"],
                "marks": 5
            },
            "q2": {
                "keywords": ["another", "answer"],
                "marks": 10
            }
        }
        self.requests = {
            "answer_set": self.answer_set,
            "question_set": self.question_set
        }

    def test_evaluate(self):
        evaluator = Evaluator(self.requests)
        expected_response = {
            "s1": {
                "q1": 5.0,
                "q2": 10.0
            },
            "s2": {
                "q1": 5.0,
                "q2": 10.0
            }
        }
        response = evaluator.evaluate()
        self.assertEqual(response, expected_response)

    def test_missing_answer_set(self):
        with self.assertRaises(ValueError):
            evaluator = Evaluator({})
            evaluator.evaluate()

    def test_missing_question_set(self):
        with self.assertRaises(ValueError):
            requests = {"answer_set": self.answer_set}
            evaluator = Evaluator(requests)
            evaluator.evaluate()

    def test_missing_keywords(self):
        question_set = {
            "q1": {
                "marks": 5.0
            }
        }
        requests = {
            "answer_set": self.answer_set,
            "question_set": question_set
        }
        with self.assertRaises(ValueError):
            evaluator = Evaluator(requests)
            evaluator.evaluate()

    def test_missing_marks(self):
        question_set = {
            "q1": {
                "keywords": ["sample", "answer"]
            }
        }
        requests = {
            "answer_set": self.answer_set,
            "question_set": question_set
        }
        with self.assertRaises(ValueError):
            evaluator = Evaluator(requests)
            evaluator.evaluate()

    def test_blank_answer(self):
        question_set = {
            "q1": {
                "keywords": ["sample", "answer"],
                "marks": 5.0
            }
        }
        answer_set = {
            "s1": {
                "q1": ""
            }
        }
        requests = {
            "answer_set": answer_set,
            "question_set": question_set
        }
        evaluator = Evaluator(requests)
        response = evaluator.evaluate()
        self.assertEqual(response["s1"]["q1"], 0.0)

    def test_invalid_answer(self):
        question_set = {
            "q1": {
                "keywords": ["sample", "answer"],
                "marks": 5.0
            }
        }
        answer_set = {
            "s1": {
                "q1": "Invalid answer."
            }
        }
        requests = {
            "answer_set": answer_set,
            "question_set": question_set
        }
        evaluator = Evaluator(requests)
        with self.assertRaises(ValueError):
            evaluator.evaluate()


if __name__ == '__main__':
    print("\n\nOutput\nRunning Unit Test for TestEvaluator")
    unittest.main()
