def findDuplicate(nums):
    variable = None
    print({*nums})
    # for i, num in enumerate(nums):
    #     if i != 0:
    #         variable = num
    #
    #         if variable == num:
    #             print("Equal", variable, num)
    #             print(num)


if __name__ == "__main__":
    findDuplicate([1, 3, 4, 2, 2])
