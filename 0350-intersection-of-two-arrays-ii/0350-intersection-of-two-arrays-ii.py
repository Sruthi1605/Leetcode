class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen = []
        used = [False] * len(nums2)  

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and not used[j]:
                    seen.append(nums2[j])
                    used[j] = True 
                    break  

        return seen