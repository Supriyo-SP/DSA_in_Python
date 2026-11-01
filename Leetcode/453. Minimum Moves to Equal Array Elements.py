class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = min(nums)
        total = 0
        for x in nums:
            total += x - m
        return total