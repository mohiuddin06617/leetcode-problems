def search(nums, target):
    len_list = len(nums)
    modified_nums = nums
    middle_point = len_list // 2

    if nums[middle_point] == target:
        return middle_point
    if len_list > 2:
        modified_nums = nums[middle_point:] if target > nums[middle_point] else nums[:middle_point]

    for i, v in enumerate(modified_nums):
        if v == target:
            return (i + middle_point) if (len_list > 2 and target > nums[middle_point]) else i
    return -1


if __name__ == '__main__':
    print(search([-1,0,5], -1))
