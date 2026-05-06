class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        i=0
        j=1
        while i<len(nums) and j<=len(nums):
            if nums[i]==nums[j]:
                return nums[i]
                break
            i+=1
            j+=1    


        """
        :type nums: List[int]
        :rtype: int
        """
        