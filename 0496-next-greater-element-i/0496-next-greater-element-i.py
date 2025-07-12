class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for num in nums1:
            found = False
            next_greater = -1
            for i in range(len(nums2)):
                if nums2[i] == num:
                    found = True
                elif found and nums2[i] > num:
                    next_greater = nums2[i]
                    break
            result.append(next_greater)
        return result