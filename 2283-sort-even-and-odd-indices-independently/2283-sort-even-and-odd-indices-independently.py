class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = sorted(nums[::2])
        odd = sorted(nums[1::2], reverse=True)
        res = []
        for i in range(len(nums)):
            res.append(even[i//2] if i % 2 == 0 else odd[i//2])
        return res