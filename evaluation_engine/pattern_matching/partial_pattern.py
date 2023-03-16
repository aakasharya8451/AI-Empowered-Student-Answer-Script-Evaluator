from jaro import jaro_winkler_metric as jaroWinkler
from editdistance import distance as editDistance
from typing import List


class PartialPatternMatching:
    def __init__(self, keyword_set: List[str], answer: str) -> None:
        """Constructor for PartialPatternMatching
        
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

    def __splittingAnswerStringInSubStrings(self, string: str, word: int) -> List[str]:
        """Splits a string into substrings of a desired word length.

        :param string: The string to split.
        :type string: str
        :param word: The desired number of words in each substring.
        :type word: int
        :return: A list of substrings.
        :rtype: list[str]
        """

        answer_substring = []

        if word == 1:
            answer_substring += string.split()
            return answer_substring

        temp_substring = string.split()

        if word > len(temp_substring):
            answer_substring.append("")
        else:
            for i in range(len(temp_substring) - (word - 1)):
                strX = ""
                for j in range(i, i + word):
                    strX += temp_substring[j] + " "
                answer_substring.append(strX[:len(strX) - 1])

        return answer_substring

    def __jaroEditMapFunction(self, jaro: float, edit: int) -> float:
        """Maps Jaro-Winkler distance and edit distance values to a value between 0 and 1
        
        :param jaro: The Jaro-Winkler distance between a keyword and a substring of the student's answer
        :type jaro: float
        :param edit: The edit distance between a keyword and a substring of the student's answer
        :type edit: int
        :return: The mapped value of Jaro-Winkler and edit distance
        :rtype: float
        """

        if jaro > 0.85 and edit < 4:
            if edit != 0:
                return jaro / edit
            else:
                return 1.0
        else:
            return 0.0

    def run(self) -> List[float]:
        """Calculates the partial pattern match value for each keyword in the keyword set
        
        :return: A list of partial pattern match values, one for each keyword in the keyword set
        :rtype: list of float
        :raises ValueError: If an error occurs during the calculation of a partial pattern match value
        """

        match_hashmap = [0.0] * len(self.keyword_set)
        for i, keyword in enumerate(self.keyword_set):
            try:
                answer_substring = self.__splittingAnswerStringInSubStrings(self.answer,
                                                                            len(keyword.split()))
                jaro_winkler_distance_hashmap = [0.0] * len(answer_substring)
                edit_distance_hashmap = [0] * len(answer_substring)

                for j in range(len(answer_substring)):
                    jaro_winkler_distance_hashmap[j] = jaroWinkler(keyword.lower(), answer_substring[j].lower())
                    edit_distance_hashmap[j] = editDistance(keyword.lower(), answer_substring[j].lower())

                combine_jaro_edit_hashmap = list(
                    map(self.__jaroEditMapFunction, jaro_winkler_distance_hashmap, edit_distance_hashmap))
                match_hashmap[i] = max(combine_jaro_edit_hashmap)

            except Exception as e:
                raise ValueError(
                    f"Error occurred at PartialPatternMatching while handling keyword at index {i}: {keyword}: {self.answer}: {e}")

        return match_hashmap


if __name__ == "__main__":
    keywords = ["Alan Turing", "alan"]
    a = "The father alam of modern computer is Ala Turin Ala Turin Ala Turing"

    x = PartialPatternMatching(keywords, a).run()
    print(x)
