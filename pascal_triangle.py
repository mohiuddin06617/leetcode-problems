from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1], [1, 1]]
        row_num = 1

        while row_num<numRows:
            # row =
            print(rows[row_num])
        # for i in range(2, numRows):
        #
        #     rows.append([1] * (i + 1))
            row_num += 1

        return rows


if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(5))
