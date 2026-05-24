class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        zeros=0
        m=0
        n=len(nums)
        left=0
        right=0
        while right<n:
            if nums[right]==0:
                zeros+=1
            if zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            if zeros<=k:
                m=max(m,right-left+1)
            right+=1               
        return m
#optimal solution     