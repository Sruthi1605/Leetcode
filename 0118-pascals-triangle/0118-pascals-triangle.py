class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for row_num in range(numRows):
            row = [1]
            if row_num > 0:
                prev_row = triangle[-1]
                for j in range(1, row_num):
                    row.append(prev_row[j - 1] + prev_row[j])
                row.append(1)
            triangle.append(row)

        return triangle