"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


def top_k_frequent(nums, k):
    temp_dict = dict()

    for index, value in enumerate(nums):
        temp_dict[value] = temp_dict.get(value, 0) + 1
        # if value not in temp_dict:
        #     temp_dict[value] = 1
        #
        # elif value in temp_dict:
        #     temp_dict[value] += 1

    keys = list({key: value for key, value in sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)}.keys())
    return keys[:k]

def top_k_frequent_two_array(nums, k):
    unique_value_list = list()
    value_counter_list = list()

    for index, value in enumerate(nums):
        if value not in unique_value_list:
            unique_value_list.append(value)
            value_counter_list.append(1)
        elif value in unique_value_list:
            index_test = unique_value_list.index(value)
            value_counter_list[index_test] += 1

from heapq import nlargest
if __name__ == '__main__':
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
    print(top_k_frequent([4, 1, -1, 2, -1, 2, 3], 2))
    # print(top_k_frequent_two_array([1, 1, 1, 2, 2, 3], 2))
