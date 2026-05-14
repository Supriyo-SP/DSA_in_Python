class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lb=-1
        hb=-1
        low=0
        n=len(nums)
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        if lb == -1 or nums[lb] != target:
            return [-1, -1] 
        low=0
        high=n-1           
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                hb=mid
                high=mid-1
            else:
                low=mid+1  
        nd = hb - 1 if hb != -1 else n - 1        
        return [lb,nd]              
