class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map = {val: idx for idx, val in enumerate(list1)}
        min_sum = float('inf')
        res = []

        for j, val in enumerate(list2):
            if val in index_map:
                total_index = index_map[val] + j
                if total_index < min_sum:
                    res = [val]
                    min_sum = total_index
                elif total_index == min_sum:
                    res.append(val)

        return res