class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num = []
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                num.append(i)
        
        if not num:
            return [-1, -1]
        else:
            return [num[0], num[-1]]
