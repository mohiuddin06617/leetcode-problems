from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = Counter(ransomNote)
        magazine_dict = Counter(magazine)
        for letter, count in ransom_dict.items():
            if letter not in magazine_dict:
                return False
            if letter in magazine_dict and count > magazine_dict.get(letter):
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.canConstruct(ransomNote="a", magazine="b"))
    print(solution.canConstruct(ransomNote="aa", magazine="ab"))
    print(solution.canConstruct(ransomNote="aa", magazine="aab"))
    print(
        solution.canConstruct(ransomNote="bg", magazine="efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj")
    )  # true
