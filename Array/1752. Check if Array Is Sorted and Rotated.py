class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s=sorted(nums)
        d=len(nums)
        for i in range (0,d):
            rotated= s[i:]+s[:i]
            if rotated== nums:
                return True 
            else:
                rotated=s    
        return False        
