class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.strip().split()
        words.reverse()
        return ' '.join(words)
        