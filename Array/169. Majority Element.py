class Solution(object):
    def majorityElement(self, nums):
        fmap=dict()
        n=len(nums)
        if n==1:
            return nums[0]
        for num in nums:
            fmap[num]=fmap.get(num,0)+1
        return max(fmap, key=fmap.get)       
        """
        :type nums: List[int]
        :rtype: int
        """
        