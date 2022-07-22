"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str):
        s_dict = dict()
        if len(s) == 0:
            return -1
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            elif letter not in s_dict:
                s_dict[letter] = 1
        for index, value in s_dict.items():
            if value == 1:
                return s.index(index)

        return -1



if __name__ == '__main__':
    solution = Solution()
    solution.firstUniqChar("leetcode")
