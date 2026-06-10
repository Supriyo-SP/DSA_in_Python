class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        if n==1:
            return 0    
        while n>1:
            if n%2==0:
                n//=2
            elif n%4==1:
                n-=1
            elif n==3:
                n-=1
            else:
                n+=1
            c+=1
        return c                    
                
