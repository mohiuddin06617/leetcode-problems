from typing import List


def max_sub_array_brute_force(nums: List[int]) -> int:
    max_sum = 0
    temp_array = list()
    enumerate_obj = enumerate(nums)
    for index, value in enumerate_obj:
        for i, v in enumerate_obj:
            max_sum += nums[i]
            # check if max_sum and store


def max_sub_array(nums: List[int]) -> int:
    """
    Kadane's Algorithm
    """
    meh = 0
    msf = -10000
    # for index, value in enumerate(nums):
    enumerate_obj = enumerate(nums)
    for i, v in enumerate_obj:
        meh = meh + nums[i]
        if meh < nums[i]:
            meh = nums[i]
        if msf < meh:
            msf = meh

    return msf


if __name__ == '__main__':
    print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_sub_array([-2, -1]))
    print(max_sub_array([-1]))
    print(max_sub_array([5, 4, -1, 7, 8]))
