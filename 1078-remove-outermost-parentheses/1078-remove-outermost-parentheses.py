class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        open=0

        for i in s:
            if i =="(":
                if open > 0:
                    res+=i
                open+=1
            elif i ==")":
                open-=1
                if open > 0:
                    res+=i
        
        return res


