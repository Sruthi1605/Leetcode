class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        result = [0] * n
        prev = float('-inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = i - prev if prev != float('-inf') else float('inf')
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            result[i] = min(result[i], prev - i if prev != float('inf') else float('inf'))
        return result