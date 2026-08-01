class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
        f , s = 1 , 2
        for step in range(3,n+1):
            curr = f+s
            f=s
            s=curr
        return curr        
                
        