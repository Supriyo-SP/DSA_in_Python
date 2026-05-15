class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        total_subset=1<<n
        res=[]
        for num in range(0,total_subset):
            ls=[]
            for i in range(0,n):
                if num &(1<<i)!=0:
                    ls.append(nums[i])
            res.append(ls)
        return res            
        