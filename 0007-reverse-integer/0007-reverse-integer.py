class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = int(str(x)[::-1]) * sign

        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev
