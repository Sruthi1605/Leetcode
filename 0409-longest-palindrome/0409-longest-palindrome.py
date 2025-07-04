class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        length = 0
        odd_found = False
        for val in count.values():
            length += (val // 2) * 2
            if val % 2 == 1:
                odd_found = True

        if odd_found:
            length += 1

        return length
        