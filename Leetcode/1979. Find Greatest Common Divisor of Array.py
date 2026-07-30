class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a=nums[0]
        b=nums[len(nums)-1]
        result=min(a,b)
        while result>0:
            if a%result==0 and b%result==0:
                break
            result-=1
        return result          
        