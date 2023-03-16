import math
from typing import List


class MarksAssigner:
    def __init__(self, fixed_match: List[float], partial_match: List[float], max_marks: int) -> None:
        """Constructor for MarksAssigner

        :param fixed_match: list containing fixed pattern match value
        :param partial_match: list containing partial pattern match value
        :param max_marks: maximum marks that can be allotted

        :raises ValueError: If any input parameter is invalid
        """

        if not isinstance(fixed_match, list) or not isinstance(partial_match, list):
            raise ValueError("fixed_match and partial_match must be lists")

        if not all(isinstance(val, float) for val in fixed_match) or not all(isinstance(val, float) for val in partial_match):
            raise ValueError(
                "fixed_match and partial_match must contain only float values")

        if not isinstance(max_marks, int) or max_marks <= 0:
            raise ValueError("max_marks must be a positive integer")

        self.fixed_match = fixed_match
        self.partial_match = partial_match
        self.max_marks = max_marks

    def assign(self) -> float:
        """Function to calculate marks

        :return: return calculated marks

        :raises ValueError: If any error occurs while calculating marks
        """

        try:
            final_match = list(map(lambda x, y: max(
                x, y), self.fixed_match, self.partial_match))
            average = sum(final_match) / len(final_match)
            marks_allotted = average * self.max_marks

            if 0.25 <= marks_allotted % math.floor(marks_allotted) < 0.75:
                return math.floor(marks_allotted) + 0.5
            else:
                return round(marks_allotted)

        except Exception as e:
            raise ValueError(
                "Error occurred while calculating marks: " + str(e))


if __name__ == "__main__":
    x = MarksAssigner([0, 1], [0.988, 1], 5).assign()
    print(x)
