import unittest
from unittest.mock import Mock
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)
from evaluation_engine.pattern_matching.fixed_pattern import FixedPatternMatching
from evaluation_engine.pattern_matching.partial_pattern import PartialPatternMatching

class TestFixedPatternMatching(unittest.TestCase):
    """
    A unit test class for the FixedPatternMatching class.
    """
    def setUp(self):
        """
        Set up the test case by creating an instance of FixedPatternMatching
        with a keyword set and an answer string.
        """
        self.keyword_set = ["Alan Turing", "alan"]
        self.answer = "The father of modern computer is Alan Turing1"

    def test_init(self):
        """
        Test the __init__ method of FixedPatternMatching by ensuring it raises
        a TypeError when invalid arguments are passed.
        """
        with self.assertRaises(TypeError):
            FixedPatternMatching("Alan Turing", self.answer)
        with self.assertRaises(TypeError):
            FixedPatternMatching(["Alan Turing", 123], self.answer)
        with self.assertRaises(TypeError):
            FixedPatternMatching(self.keyword_set, 123)
        with self.assertRaises(TypeError):
            FixedPatternMatching(123, self.answer)

    def test_regExSearch(self):
        """
        Test the __regExSearch method of FixedPatternMatching by checking its
        output for various inputs.
        """
        fpm = FixedPatternMatching(self.keyword_set, self.answer)
        self.assertTrue(fpm._FixedPatternMatching__regExSearch('Alan Turing', self.answer))
        self.assertFalse(fpm._FixedPatternMatching__regExSearch('Tim Berners-Lee', self.answer))

    def test_run_with_single_keyword_and_answer(self):
        keyword_set = ["alan"]
        fpm = FixedPatternMatching(keyword_set, self.answer)
        match_values = fpm.run()
        self.assertEqual(match_values, [1.0]) 

    def test_run_with_multiple_keywords_and_answer(self):
        """
        Test the run method of FixedPatternMatching by comparing the output
        to an expected result.
        """
        fpm = FixedPatternMatching(self.keyword_set, self.answer)
        match_values = fpm.run()
        self.assertEqual(match_values, [1.0, 1.0])


if __name__ == '__main__':
    print("\n\nOutput\nRunning Unit Test for TestFixedPatternMatching")
    unittest.main()
    print("Test End\n\n\n")
