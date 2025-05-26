class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zeros = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeros.append((i, j))

        for r, c in zeros:
            for i in range(cols):
                matrix[r][i] = 0
            for i in range(rows):
                matrix[i][c] = 0