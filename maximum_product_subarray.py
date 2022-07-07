from typing import List


class Solution:
    def max_product(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_ending_here = nums[0]

        for index in range(1, len(nums)):
            max_ending_here = max_ending_here * nums[index]

            if max_ending_here < nums[index]:
                max_ending_here = nums[index]

            if max_so_far < max_ending_here:
                max_so_far = max_ending_here

        return max_so_far


def test(nums):
    max = nums[0]
    prev = None
    for num in nums[1:]:
        temp = max * num
        prev = num
        if temp > max:
            max = temp

    return max


if __name__ == "__main__":
    solution = Solution()

    # print(solution.max_product([-2]))
    print(test([2, 3, -2, 4]))
    # print(solution.maxProduct([-2, 0, -1]))
    # print(test([-3, -1, -1]))
    # print(test([-2, 3, -4]))
