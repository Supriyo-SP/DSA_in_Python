class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        target = nums[n//2]
        total = 0
        for x in nums:
            total += abs(x-target)
        return total
        