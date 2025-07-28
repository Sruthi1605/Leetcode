class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = m2 = -1
        idx = -1
        for i, x in enumerate(nums):
            if x > m1:
                m2, m1, idx = m1, x, i
            elif x > m2:
                m2 = x
        return idx if m1 >= 2 * m2 else -1