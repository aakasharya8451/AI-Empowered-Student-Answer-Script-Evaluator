# import unittest
# from unittest.mock import Mock
# import sys
# import os

# # Add current working directory to sys path to access modules
# current_working_directory = os.getcwd()
# sys.path.insert(0, current_working_directory)
# from evaluation_engine.pattern_matching.fixed_pattern import FixedPatternMatching
# from evaluation_engine.pattern_matching.partial_pattern import PartialPatternMatching
# from evaluation_engine.marks_assigner.marks_assigner import MarksAssigner
# from evaluation_engine.evaluator import Evaluator


# class TestFixedPatternMatching(unittest.TestCase):
#     """
#     A unit test class for the FixedPatternMatching class.
#     """
#     def setUp(self):
#         """
#         Set up the test case by creating an instance of FixedPatternMatching
#         with a keyword set and an answer string.
#         """
#         self.keyword_set = ["Alan Turing", "alan"]
#         self.answer = "The father of modern computer is Alan Turing1"

#     def test_init(self):
#         """
#         Test the __init__ method of FixedPatternMatching by ensuring it raises
#         a TypeError when invalid arguments are passed.
#         """
#         with self.assertRaises(TypeError):
#             FixedPatternMatching("Alan Turing", self.answer)
#         with self.assertRaises(TypeError):
#             FixedPatternMatching(["Alan Turing", 123], self.answer)
#         with self.assertRaises(TypeError):
#             FixedPatternMatching(self.keyword_set, 123)
#         with self.assertRaises(TypeError):
#             FixedPatternMatching(123, self.answer)

#     def test_regExSearch(self):
#         """
#         Test the __regExSearch method of FixedPatternMatching by checking its
#         output for various inputs.
#         """
#         fpm = FixedPatternMatching(self.keyword_set, self.answer)
#         self.assertTrue(fpm._FixedPatternMatching__regExSearch('Alan Turing', self.answer))
#         self.assertFalse(fpm._FixedPatternMatching__regExSearch('Tim Berners-Lee', self.answer))

#     def test_run_with_single_keyword_and_answer(self):
#         keyword_set = ["alan"]
#         pp = PartialPatternMatching(keyword_set, self.answer)
#         match_values = pp.run()
#         self.assertEqual(match_values, [1.0]) 

#     def test_run_with_multiple_keywords_and_answer(self):
#         """
#         Test the run method of FixedPatternMatching by comparing the output
#         to an expected result.
#         """
#         fpm = FixedPatternMatching(self.keyword_set, self.answer)
#         match_values = fpm.run()
#         self.assertEqual(match_values, [1.0, 1.0])


# class TestPartialPatternMatching(unittest.TestCase):
#     def setUp(self):
#         """
#         Set up the test case by creating an instance of FixedPatternMatching
#         with a keyword set and an answer string.
#         """
#         self.keyword_set = ["Alan Turing", "alan"]
#         self.answer = "The father of modern computer is Alan Turing1"

#     def test_init(self):
#         with self.assertRaises(TypeError):
#             PartialPatternMatching([1, 2, 3], self.answer)
#         with self.assertRaises(TypeError):
#             PartialPatternMatching(["sample", "keywords", 123], self.answer)
#         with self.assertRaises(TypeError):
#             PartialPatternMatching(self.keyword_set, 123)
#         with self.assertRaises(TypeError):
#             PartialPatternMatching(self.keyword_set, "")

#     def test_splitting_answer_string_into_substrings(self):
#         test_string_split = "The quick brown fox jumps over the lazy dog"
#         pp = PartialPatternMatching([], "The quick brown fox jumps over the lazy dog")
#         substrings = pp._PartialPatternMatching__splittingAnswerStringInSubStrings(test_string_split, 1)
#         self.assertEqual(substrings, ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'])
#         substrings = pp._PartialPatternMatching__splittingAnswerStringInSubStrings(test_string_split, 2)
#         self.assertEqual(substrings, ['The quick', 'quick brown', 'brown fox', 'fox jumps', 'jumps over', 'over the', 'the lazy', 'lazy dog'])
#         substrings = pp._PartialPatternMatching__splittingAnswerStringInSubStrings(test_string_split, 3)
#         self.assertEqual(substrings, ['The quick brown', 'quick brown fox', 'brown fox jumps', 'fox jumps over', 'jumps over the', 'over the lazy', 'the lazy dog'])
#         substrings = pp._PartialPatternMatching__splittingAnswerStringInSubStrings(test_string_split, len(test_string_split.split()))
#         self.assertEqual(substrings, ['The quick brown fox jumps over the lazy dog'])
#         substrings = pp._PartialPatternMatching__splittingAnswerStringInSubStrings(test_string_split, len(test_string_split.split())+1)
#         self.assertEqual(substrings, [''])

#     def test_jaro_edit_map_function(self):
#         pp = PartialPatternMatching(self.keyword_set, self.answer)
#         mapped_value = pp._PartialPatternMatching__jaroEditMapFunction(0.9, 2)
#         self.assertEqual(mapped_value, 0.45)

#     def test_run_with_single_keyword_and_answer(self):
#         keywords = ["sample"]
#         answer = "This is a sample answer"
#         pp = PartialPatternMatching(keywords, answer)
#         match_values = pp.run()
#         self.assertEqual(match_values, [1.0])

#     def test_run_with_multiple_keywords_and_answer(self):
#         keywords = ["computer", "science", "study"]
#         answer = "Compute Scien is the study of computers and computational systems"
#         pp = PartialPatternMatching(keywords, answer)
#         match_values = pp.run()
#         self.assertAlmostEqual(round(match_values[0], 2), 0.98)
#         self.assertAlmostEqual(round(match_values[1], 2), 0.47)
#         self.assertAlmostEqual(round(match_values[2], 2), 1.0)


# class TestMarksAssigner(unittest.TestCase):
#     def test_valid_input(self):
#         ma = MarksAssigner([0.5, 0.75], [0.8, 0.9], 10)
#         self.assertEqual(ma.assign(), 8.5)

#     def test_invalid_fixed_match(self):
#         with self.assertRaises(ValueError):
#             MarksAssigner("invalid", [0.8, 0.9], 10)

#     def test_invalid_partial_match(self):
#         with self.assertRaises(ValueError):
#             MarksAssigner([0.5, 0.75], "invalid", 10)

#     def test_invalid_max_marks(self):
#         with self.assertRaises(ValueError):
#             MarksAssigner([0.5, 0.75], [0.8, 0.9], -10)








# class TestEvaluator(unittest.TestCase):

#     def setUp(self):
#         self.answer_set = {
#             "s1": {
#                 "q1": "This is a sample answer.",
#                 "q2": "Another sample answer.",
#             },
#             "s2": {
#                 "q1": "Sample answer for question 1.",
#                 "q2": "Yet another sample answer.",
#             }
#         }
#         self.question_set = {
#             "q1": {
#                 "keywords": ["sample", "answer"],
#                 "marks": 5
#             },
#             "q2": {
#                 "keywords": ["another", "answer"],
#                 "marks": 10
#             }
#         }
#         self.requests = {
#             "answer_set": self.answer_set,
#             "question_set": self.question_set
#         }

#     def test_evaluate(self):
#         evaluator = Evaluator(self.requests)
#         expected_response = {
#             "s1": {
#                 "q1": 5.0,
#                 "q2": 10.0
#             },
#             "s2": {
#                 "q1": 5.0,
#                 "q2": 10.0
#             }
#         }
#         response = evaluator.evaluate()
#         self.assertEqual(response, expected_response)

#     def test_missing_answer_set(self):
#         with self.assertRaises(ValueError):
#             evaluator = Evaluator({})
#             evaluator.evaluate()

#     def test_missing_question_set(self):
#         with self.assertRaises(ValueError):
#             requests = {"answer_set": self.answer_set}
#             evaluator = Evaluator(requests)
#             evaluator.evaluate()

#     def test_missing_keywords(self):
#         question_set = {
#             "q1": {
#                 "marks": 5.0
#             }
#         }
#         requests = {
#             "answer_set": self.answer_set,
#             "question_set": question_set
#         }
#         with self.assertRaises(ValueError):
#             evaluator = Evaluator(requests)
#             evaluator.evaluate()

#     def test_missing_marks(self):
#         question_set = {
#             "q1": {
#                 "keywords": ["sample", "answer"]
#             }
#         }
#         requests = {
#             "answer_set": self.answer_set,
#             "question_set": question_set
#         }
#         with self.assertRaises(ValueError):
#             evaluator = Evaluator(requests)
#             evaluator.evaluate()

#     def test_blank_answer(self):
#         question_set = {
#             "q1": {
#                 "keywords": ["sample", "answer"],
#                 "marks": 5.0
#             }
#         }
#         answer_set = {
#             "s1": {
#                 "q1": ""
#             }
#         }
#         requests = {
#             "answer_set": answer_set,
#             "question_set": question_set
#         }
#         evaluator = Evaluator(requests)
#         response = evaluator.evaluate()
#         self.assertEqual(response["s1"]["q1"], 0.0)

#     def test_invalid_answer(self):
#         question_set = {
#             "q1": {
#                 "keywords": ["sample", "answer"],
#                 "marks": 5.0
#             }
#         }
#         answer_set = {
#             "s1": {
#                 "q1": "Invalid answer."
#             }
#         }
#         requests = {
#             "answer_set": answer_set,
#             "question_set": question_set
#         }
#         evaluator = Evaluator(requests)
#         with self.assertRaises(ValueError):
#             evaluator.evaluate()


# if __name__ == '__main__':
#     unittest.main()












# if __name__ == "__main__":
#     unittest.main()










# import unittest
# import sys
# import os

# # Add current working directory to sys path to access modules
# current_working_directory = os.getcwd()
# sys.path.insert(0, current_working_directory)
# from evaluation_engine.evaluator import Evaluator


# class EvaluationEngineIntegrationTest(unittest.TestCase):
#     def test_evaluate(self):
#         requests = {
#             "question_set": {
#                 "q1": {"keywords": ["Alan Turing", "alan"], "marks": 10},
#                 "q2": {"keywords": ["Charles Babbage", "Charles"], "marks": 2}
#             },
#             "answer_set": {
#                 "s1": {"q1": "The father alam of modern computer is Ala Turin Ala Turin Ala Turing",
#                        "q2": "The father of computer is Charles Babbage"},
#                 "s2": {"q1": "",
#                        "q2": ""}
#             }
#         }

#         expected_output = {
#             "s1": {"q1": 9.5, "q2": 2.0},
#             "s2": {"q1": 0.0, "q2": 0.0}
#         }

#         evaluator = Evaluator(requests)
#         actual_output = evaluator.evaluate()

#         self.assertEqual(expected_output, actual_output)

# if __name__ == "__main__":
#     print("\n\nOutput\nRunning Integration Test for EvaluationEngineIntegrationTest")
#     unittest.main()

import unittest
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)
from evaluation_engine.evaluator import Evaluator


class EvaluationEngineIntegrationTest(unittest.TestCase):
    def test_evaluate_with_valid_requests(self):
        # Arrange
        requests = {
            "question_set": {
                "q1": {"keywords": ["Alan Turing", "alan"], "marks": 10},
                "q2": {"keywords": ["Charles Babbage", "Charles"], "marks": 2}
            },
            "answer_set": {
                "s1": {"q1": "The father alam of modern computer is Ala Turin Ala Turin Ala Turing",
                       "q2": "The father of computer is Charles Babbage"},
                "s2": {"q1": "It is a sample answer",
                       "q2": "It is a wrong answer"}
            }
        }

        expected_output = {
            "s1": {"q1": 9.5, "q2": 2.0},
            "s2": {"q1": 0.0, "q2": 0.0}
        }

        # Act
        evaluator = Evaluator(requests)
        actual_output = evaluator.evaluate()

        # Assert
        self.assertEqual(expected_output, actual_output)

    def test_evaluate_with_missing_answer_set(self):
        # Arrange
        requests = {
            "question_set": {
                "q1": {"keywords": ["Alan Turing", "alan"], "marks": 10},
                "q2": {"keywords": ["Charles Babbage", "Charles"], "marks": 2}
            },
        }

        # Act and Assert
        with self.assertRaises(ValueError):
            evaluator = Evaluator(requests)
            evaluator.evaluate()

    def test_evaluate_with_missing_question_set(self):
        # Arrange
        requests = {
            "answer_set": {
                "s1": {"q1": "The father alam of modern computer is Ala Turin Ala Turin Ala Turing",
                       "q2": "The father of computer is Charles Babbage"},
                "s2": {"q1": "",
                       "q2": ""}
            }
        }

        # Act and Assert
        with self.assertRaises(ValueError):
            evaluator = Evaluator(requests)
            evaluator.evaluate()

if __name__ == "__main__":
    print("\n\nOutput\nRunning Integration Test for EvaluationEngineIntegrationTest")
    unittest.main()
