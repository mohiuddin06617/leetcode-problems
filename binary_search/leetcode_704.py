def search(nums, target):
    low = 0
    list_length = len(nums) - 1
    middle_point = list_length // 2
    if middle_point == target:
        return middle_point
    for num in nums:
        if target > middle_point:
            print(i)






if __name__ == '__main__':
    search([1, 2, 3, 5, 8], 6)
