import unittest
from unittest.mock import Mock
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)
from evaluation_engine.marks_assigner.marks_assigner import MarksAssigner


class TestMarksAssigner(unittest.TestCase):
    def test_valid_input(self):
        ma = MarksAssigner([0.5, 0.75], [0.8, 0.9], 10)
        self.assertEqual(ma.assign(), 8.5)

    def test_invalid_fixed_match(self):
        with self.assertRaises(ValueError):
            MarksAssigner("invalid", [0.8, 0.9], 10)

    def test_invalid_partial_match(self):
        with self.assertRaises(ValueError):
            MarksAssigner([0.5, 0.75], "invalid", 10)

    def test_invalid_max_marks(self):
        with self.assertRaises(ValueError):
            MarksAssigner([0.5, 0.75], [0.8, 0.9], -10)


if __name__ == "__main__":
    print("\n\nOutput\nRunning Unit Test for TestMarksAssigner")
    unittest.main()