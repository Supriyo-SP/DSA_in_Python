class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        h={}
        m=d=-1
        for num in nums:
            h[num]=h.get(num,0)+1
        for i in range(1,len(nums)+1):
            count = h.get(i, 0)
            if count==0:
                m=i
            elif count==2:
                d=i
        return [d,m]           


        