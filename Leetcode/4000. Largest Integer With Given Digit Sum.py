class Solution(object):
    def largestInteger(self, n, s):
        """
        :type n: int
        :type s: int
        :rtype: int
        """
        if s==0:
            return 0
        if s>9*n:
            return -1
        res=[]
        for i in range(n):
            d=min(9 , s)
            res.append(str(d))
            s -= d
        return int("".join(res))
            