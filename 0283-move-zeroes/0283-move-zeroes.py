class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp=[]
        i=0
        while i < len(nums):
            if nums[i]==0:
                temp.append(nums[i])
                nums.pop(i)
            else:
                i+=1
        nums.extend(temp)


        