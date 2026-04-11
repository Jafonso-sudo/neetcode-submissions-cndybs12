class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n

        while l < r:
            k = (l + r) // 2
            i = k // n
            j = k % n
            num = matrix[i][j]
            if num == target:
                return True
            elif num < target:
                l = k + 1
            else:
                r = k

        return False