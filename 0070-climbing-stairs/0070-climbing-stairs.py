class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=1
        y=1

        for i in range(n):
            x, y = y, x + y
        return x