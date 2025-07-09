class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        score_with_index = list(enumerate(score))
       
        score_with_index.sort(key=lambda x: -x[1])

        res = [""] * len(score)

        for i, (idx, _) in enumerate(score_with_index):
            if i == 0:
                res[idx] = "Gold Medal"
            elif i == 1:
                res[idx] = "Silver Medal"
            elif i == 2:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(i + 1)

        return res
        