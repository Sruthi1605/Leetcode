class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        merged = []
        for current in intervals:
            if current[1] < newInterval[0]:
                merged.append(current)
            elif current[0] > newInterval[1]:
                merged.append(newInterval)
                newInterval = current
            else:
                newInterval[0] = min(newInterval[0], current[0])
                newInterval[1] = max(newInterval[1], current[1])
        merged.append(newInterval)
        return merged