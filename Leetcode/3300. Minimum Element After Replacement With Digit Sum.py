class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls=[]
        for num in nums:
            s=0
            while num>0:
                d=num%10
                s+=d
                num=num//10
            ls.append(s)    
        return min(ls)        



        