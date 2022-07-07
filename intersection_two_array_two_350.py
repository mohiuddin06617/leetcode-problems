from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    temp_dict = {}
    result = []

    for num in nums1:
        if num not in temp_dict:
            temp_dict[num] = 1
        else:
            temp_dict[num] += 1
    temp_dict_keys = temp_dict.keys()

    for num in nums2:
        if num in temp_dict:
            result.append(num)
            if temp_dict[num] == 1:
                temp_dict.pop(num)
            else:
                temp_dict[num] -= 1
    return result


if __name__ == '__main__':
    print(intersect([1, 2, 2, 1], [2, 2]))
    print(intersect([1, 2, 2, 1], [2]))  # expected [2]
    print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
    print(intersect([1, 2, 2, 1], [1, 1]))  # expected [1,1]
