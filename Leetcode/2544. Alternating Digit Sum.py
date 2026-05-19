class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        e=0
        o=0
        l=len(str(n))
        if l==1:
            return n
        for i,d in enumerate(str(n)):
            if i%2==0:
                e+=int(d)
            else:
                o+=int(d)    
        return e-o

        