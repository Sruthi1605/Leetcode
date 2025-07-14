class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        total = len(mat) * len(mat[0])
        
        if total != r * c:
            return mat

        flat = [num for row in mat for num in row]

        return [flat[i * c : (i + 1) * c] for i in range(r)]