from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(1, numRows):
            rows.append([])
            rows[i].append(1)

            for j in range(1, i):
                rows[i].append(rows[i - 1][j - 1] + rows[i - 1][j])
            if numRows != 0:
                rows[i].append(1)

        return rows


if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(20))
