class Solution(object):
    def maximumGap(self, nums):
        l=len(nums)
        nums.sort()
        if l <= 1:
            return 0
        maxi=0
        i=0    
        while i<l-1:
            d=nums[i+1]-nums[i]
            maxi=max(maxi,d)
            i+=1
        return maxi    

        """
        :type nums: List[int]
        :rtype: int
        """
        