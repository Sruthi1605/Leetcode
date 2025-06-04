class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""
        while columnNumber > 0:
            columnNumber -= 1  
            result = chr(columnNumber % 26 + ord('A')) + result
            columnNumber //= 26
        return result
        