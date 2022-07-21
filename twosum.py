from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int):
        # return next([i, j] for i, x in enumerate(nums) for j, y in enumerate(nums) if i != j and x + y == target)
        num_len = len(nums)
        for i in range(num_len):
            for j in range(num_len):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

    def two_sum_optimized_hashmap(self, nums, target):
        for index, number in enumerate(nums):
            req_number = target - number
            temp_list = nums[(index+1):]
            if req_number in temp_list:
                return [index, nums.index(req_number, index+1)]


if __name__ == "__main__":
    solution = Solution()
    # print(solution.two_sum_optimized_hashmap([2,7,11,15], 9))
    print(solution.two_sum_optimized_hashmap([3, 2, 3], 6))
    # print(solution.two_sum_optimized_hashmap([3, 2, 4], 6))
