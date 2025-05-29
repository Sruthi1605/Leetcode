class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            sum = 0
            for i in str(num):
                sum += int(i)
            num = sum  
        return num