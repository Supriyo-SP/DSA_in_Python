class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        while n%4==0:
            n=n/4
        if n==1:
            return True
        return False        
                
        