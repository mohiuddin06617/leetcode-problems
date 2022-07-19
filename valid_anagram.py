"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp_dict = {}
        # result =
        if len(s) != len(t):
            return False

        for letter in t:
            temp_dict[letter] = letter
        for letter in s:
            if letter not in temp_dict:
                return False

        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram(s="anagram", t="nagaram"))  # true
    print(solution.isAnagram(s="rat", t="car"))  # false
    print(solution.isAnagram(s="ab", t="a"))  # false
