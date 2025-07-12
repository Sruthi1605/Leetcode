class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        w = int(math.sqrt(area)) 
        while area % w != 0:
            w -= 1
        return [area // w, w]