class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            large = max(nums[:i+1])
            small = min(nums[i:])
            score = large - small
            if score <= k:
                return i
        return -1

        