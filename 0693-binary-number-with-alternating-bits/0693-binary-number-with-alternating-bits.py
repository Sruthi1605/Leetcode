class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b=bin(n)[2:]
        for i in range(len(b)-1):
            if b[i] == b[i+1]:
                return False
        
        return True