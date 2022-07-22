"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        s_len = len(s)
        if s_len != len(t):
            return False

        for index in range(s_len):
            if s[index] in s_dict:
                s_dict[s[index]] += 1
            else:
                s_dict[s[index]] = 1

            if t[index] in t_dict:
                t_dict[t[index]] += 1
            else:
                t_dict[t[index]] = 1

        for letter, value in s_dict.items():
            if t_dict.get(letter) is None or t_dict.get(letter) != s_dict.get(letter):
                return False

        return True

    def is_anagram_shorter(self, s:str, t:str) -> bool:
        s_dict = {}
        t_dict = {}

        s_len = len(s)

        if s_len != len(t):
            return False

        for index in range(s_len):
            s_dict[s[index]] = s_dict.get(s[index], 0) + 1

            t_dict[t[index]] = t_dict.get(t[index], 0) + 1

        return s_dict == t_dict



if __name__ == "__main__":
    solution = Solution()
    # print(solution.isAnagram(s="anagram", t="nagaram"))  # true
    # print(solution.isAnagram(s="rat", t="car"))  # false
    print(solution.isAnagram(s="ab", t="a"))  # false
    print(solution.is_anagram_shorter(s="ab", t="a"))  # false
    # print(solution.isAnagram(s="aacc", t="ccac"))  # false
