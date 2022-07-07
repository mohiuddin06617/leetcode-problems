from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    # nums1 = list(set(nums1))
    # if nums1[0] == 0:
    #     nums1.pop(0)
    #
    # return list(set([*nums1, *set(nums2)]))
    nums1_len = ((m + n))
    temp_nums1 = list()
    for index in range(nums1_len):
        if nums1[index] != 0:
            temp_nums1.append(nums1[index])

    for index in range(n):
        if nums2[index] != 0:
            temp_nums1.append(nums2[index])

    nums1 = sorted(temp_nums1)
    return nums1


def merge_test(nums1: List[int], m: int, nums2: List[int], n: int):
    nums1 = list(filter(lambda num: num != 0, nums1))
    nums2 = list(filter(lambda num: num != 0, nums2))
    nums1 = sorted([*nums1, *nums2])
    return nums1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    print(merge_test(nums1, m, nums2, n))

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(merge_test(nums1, m, nums2, n))

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(merge_test(nums1, m, nums2, n))
