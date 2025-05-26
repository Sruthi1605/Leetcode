class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_water = 0
        
        while left < right:
            
            width = right - left
            min_height = min(height[left], height[right])
            area = width * min_height
            max_water = max(max_water, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water