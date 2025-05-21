class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack=[]

        for c in s:
            if stack and c.swapcase() == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)
