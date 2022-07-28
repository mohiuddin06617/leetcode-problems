from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found = False
        probable_row = None

        for index, matrix_row in enumerate(matrix):
            if matrix_row[0] <= target <= matrix_row[-1]:
                probable_row = index
                found = True

        if found is False and probable_row is None:
            return found

        for index, value in enumerate(matrix[probable_row]):
            if value == target:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
    print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
