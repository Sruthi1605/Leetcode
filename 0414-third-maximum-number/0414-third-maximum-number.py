class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))         
        nums.sort(reverse=True)        
        if len(nums) >= 3:
            return nums[2]             
        else:
            return nums[0] 