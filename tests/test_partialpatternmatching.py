import unittest
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)
from evaluation_engine.pattern_matching.partial_pattern import PartialPatternMatching


class TestPartialPatternMatching(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case by creating an instance of FixedPatternMatching
        with a keyword set and an answer string.
        """
        self.keyword_set = ["Alan Turing", "alan"]
        self.answer = "The father of modern computer is Alan Turing1"

    def test_init(self):
        with self.assertRaises(TypeError):
            PartialPatternMatching([1, 2, 3], self.answer)
        with self.assertRaises(TypeError):
            PartialPatternMatching(["sample", "keywords", 123], self.answer)
        with self.assertRaises(TypeError):
            PartialPatternMatching(self.keyword_set, 123)
        with self.assertRaises(TypeError):
            PartialPatternMatching(self.keyword_set, "")

    def test_splitting_answer_string_into_substrings(self):
        test_string_split = "The quick brown fox jumps over the lazy dog"
        pp = PartialPatternMatching([], "The quick brown fox jumps over the lazy dog")
        substrings = pp._PartialPatternMatching__splittingAnswerStringInSubStrings(test_string_split, 1)
        self.assertEqual(substrings, ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'])
        substrings = pp._PartialPatternMatching__splittingAnswerStringInSubStrings(test_string_split, 2)
        self.assertEqual(substrings, ['The quick', 'quick brown', 'brown fox', 'fox jumps', 'jumps over', 'over the', 'the lazy', 'lazy dog'])
        substrings = pp._PartialPatternMatching__splittingAnswerStringInSubStrings(test_string_split, 3)
        self.assertEqual(substrings, ['The quick brown', 'quick brown fox', 'brown fox jumps', 'fox jumps over', 'jumps over the', 'over the lazy', 'the lazy dog'])
        substrings = pp._PartialPatternMatching__splittingAnswerStringInSubStrings(test_string_split, len(test_string_split.split()))
        self.assertEqual(substrings, ['The quick brown fox jumps over the lazy dog'])
        substrings = pp._PartialPatternMatching__splittingAnswerStringInSubStrings(test_string_split, len(test_string_split.split())+1)
        self.assertEqual(substrings, [''])

    def test_jaro_edit_map_function(self):
        pp = PartialPatternMatching(self.keyword_set, self.answer)
        mapped_value = pp._PartialPatternMatching__jaroEditMapFunction(0.9, 2)
        self.assertEqual(mapped_value, 0.45)

    def test_run_with_single_keyword_and_answer(self):
        keywords = ["sample"]
        answer = "This is a sample answer"
        pp = PartialPatternMatching(keywords, answer)
        match_values = pp.run()
        self.assertEqual(match_values, [1.0])

    def test_run_with_multiple_keywords_and_answer(self):
        keywords = ["computer", "science", "study"]
        answer = "Compute Scien is the study of computers and computational systems"
        pp = PartialPatternMatching(keywords, answer)
        match_values = pp.run()
        self.assertAlmostEqual(round(match_values[0], 2), 0.98)
        self.assertAlmostEqual(round(match_values[1], 2), 0.47)
        self.assertAlmostEqual(round(match_values[2], 2), 1.0)


if __name__ == '__main__':
    print("\n\nOutput\nRunning Unit Test for TestPartialPatternMatching")
    unittest.main()

