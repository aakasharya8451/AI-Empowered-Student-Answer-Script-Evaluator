from re import search, IGNORECASE
from typing import List


class FixedPatternMatching:
    def __init__(self, keyword_set: List[str], answer: str) -> None:
        """Constructor for FixedPatternMatching
        
        :param keyword_set: list containing all keywords related to answer
        :type keyword_set: List[str]
        :param answer: student answer string
        :type answer: str
        :raises TypeError: if keyword_set is not a list of strings or answer is not a string
        """
        if not isinstance(keyword_set, list):
            raise TypeError("Keyword set must be a list of strings")

        for keyword in keyword_set:
            if not isinstance(keyword, str):
                raise TypeError(
                    "All keywords in the keyword set must be strings")

        if not isinstance(answer, str):
            raise TypeError("Answer must be a string")

        self.keyword_set = keyword_set
        self.answer = answer

    def __regExSearch(self, pattern: str, string: str) -> bool:
        """Private function to perform regex search for the given pattern in the given string.

        :param pattern: pattern string
        :param string: answer string
        :return: True if pattern is found in string, False otherwise
        :rtype: bool
        """

        matches = search(pattern, string, IGNORECASE)
        flag = True if matches is not None else False
        return flag

    def run(self) -> list[float]:
        """Function to find the fixed pattern match value for each keyword in the keyword set.

        :return: A list of fixed pattern match values, one for each keyword in the keyword set
        :rtype: list of float
        :raises ValueError: If an error occurs during the calculation of a partial pattern match value
        """

        match_hashmap = [0] * len(self.keyword_set)

        for i, keyword in enumerate(self.keyword_set):
            try:
                if self.__regExSearch(keyword, self.answer):
                    match_hashmap[i] = 1.0
                else:
                    match_hashmap[i] = 0.0

            except Exception as e:
                raise ValueError(
                    f"Error occurred at FixedPatternMatching while handling keyword at index {i}: {keyword}: {self.answer}: {e}")

        return match_hashmap


if __name__ == "__main__":
    test = FixedPatternMatching(
        ["Alan Turing", "alan"], "The father of modern computer is Alan Turing1").run()
    print(test)
