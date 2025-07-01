class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen=[]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j] and nums1[i] not in seen:
                    seen.append(nums1[i])

        return seen