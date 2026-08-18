class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_idx = 0
        for i in range(len(nums)):
            if i > max_idx :
                return False
                break
            max_idx = max(max_idx ,(i + nums[i]))
        return True
