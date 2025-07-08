class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = (1 << num.bit_length()) - 1
        return mask ^ num