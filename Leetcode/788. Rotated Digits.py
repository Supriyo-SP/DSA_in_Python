class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        for i in range(0,n+1):
            haschange=False
            isvalid=True
            cnum=i
            while cnum>0:
                d=cnum%10
                if d==3 or d==4 or d==7:
                    isvalid=False
                    break
                if d==2 or d==5 or d==6 or d==9:
                    haschange=True 
                cnum//=10
            if haschange and isvalid:
                c+=1
        return c

        