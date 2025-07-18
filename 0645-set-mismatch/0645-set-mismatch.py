class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        total = sum(set(nums))
        actual = sum(nums)
        expected = n * (n + 1) // 2

        duplicate = actual - total
        missing = expected - total
        return [duplicate, missing]
