from typing import List
from collections import Counter


def contains_duplicate(nums: List[int]):
    items = Counter(nums).items()
    status = False
    for key, value in items:
        print(value)
        if value >= 2:
            status = True
        pass
    return status

def contains_duplicate_one_line_set(nums: List[int]):
    return len(set(nums)) != len(nums)

if __name__ == "__main__":
    print(contains_duplicate([2, 14, 18, 22, 22]))
