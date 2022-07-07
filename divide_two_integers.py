class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return dividend<<abs(divisor)

class Test:
    def divide(self, dividend: int, divisor: int) -> int:
        counter = 0
        abs_divisor = abs(divisor)
        abs_dividend = abs(dividend)

        if dividend == (2 ** 31 - 1) and abs_divisor == 1:
            return (2**31-1) if self.neg_checker(divisor) else -(2**31-1)
        elif dividend == -2 ** 31 and abs_divisor == 1:
            return (2 ** 31 - 1) if not self.neg_checker(divisor) else -2**31

        if abs_dividend == abs_divisor:
            if (self.neg_checker(dividend) and self.neg_checker(divisor)) or (
                    not self.neg_checker(dividend) and not self.neg_checker(divisor)):
                return 1
            elif (not self.neg_checker(dividend) and self.neg_checker(divisor)) or (
                    self.neg_checker(dividend) and not self.neg_checker(divisor)):
                return -1
        while abs_divisor < abs_dividend:
            abs_dividend -= abs_divisor
            counter += 1
        return -counter if divisor < 0 else counter

    def neg_checker(self, val):
        return True if val > 0 else False


if __name__ == '__main__':
    solution = Solution()
    print(solution.divide(10, 3))

    # Driver code
    # a = 10
    # b = 3
    # print(divide(a, b))
    #
    # a = 43
    # b = -8
    # print(divide(a, b))

    test = Test()
    a = 2147483647
    b = 2
    # print(test.divide(a, b))