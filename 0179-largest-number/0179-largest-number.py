class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        nums.sort(cmp=lambda a, b: -1 if a + b > b + a else 1 if a + b < b + a else 0)
        result = ''.join(nums)
        return '0' if result[0] == '0' else result

        